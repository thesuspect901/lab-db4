import os

from dotenv import load_dotenv
load_dotenv()

from datetime import timedelta
import mysql.connector as sql_connector

from flasgger import Swagger

from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity  


app = Flask(__name__)
bcrypt = Bcrypt(app)

# ----- Конфіг ----- #
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'admin')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'lab4')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', 3306))
app.config['MYSQL_SSL_DISABLED'] = True

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'supersecretkey')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)
jwt = JWTManager(app)

mysql = MySQL(app)
app.mysql = mysql

def init_db():
    """Перевіряє, чи існує БД lab4, якщо ні — створює"""
    try:
        conn = sql_connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            port=os.getenv('MYSQL_PORT', 3306)
        )
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS lab4;")
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Database lab4 ensured.")
    except Exception as e:
        print("❌ Database init error:", e)

init_db()

try:
    from auth.route import user_bp, story_bp, media_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(story_bp)
    app.register_blueprint(media_bp)
    print("✅ Blueprints loaded successfully.")
except Exception as e:
    print("❌ Blueprint import error:", e)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Lab4 API",
        "description": "API documentation for Users, Stories and Media",
        "version": "1.0.0"
    }
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

Swagger(app, config=swagger_config, template=swagger_template)

@app.route('/health')
def health():
    return {"status": "ok"}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not username or not password or not email:
        return jsonify({"error": "Missing username, password, or email"}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Users (username, password, email) VALUES (%s, %s, %s)", 
                (username, hashed_pw, email))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    cur = mysql.connection.cursor()
    cur.execute("SELECT user_id, password FROM Users WHERE username=%s", (username,))
    user = cur.fetchone()
    cur.close()

    if not user or not bcrypt.check_password_hash(user[1], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"user_id": user[0], "username": username})
    return jsonify({"access_token": access_token}), 200

@app.route('/secure', methods=['GET'])
@jwt_required()
def secure():
    user = get_jwt_identity()
    return jsonify({
        "message": f"Welcome, {user['username']}! You have access to protected data."
    }), 200

@app.route('/stories', methods=['GET'])
def get_stories():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT s.story_id, u.username, s.created_at
        FROM Stories s
        JOIN Users u ON s.user_id = u.user_id
        ORDER BY s.created_at DESC
    """)
    stories = [{"story_id": sid, "username": uname, "created_at": str(created)} 
               for sid, uname, created in cur.fetchall()]
    cur.close()
    return jsonify(stories)

@app.route('/stories', methods=['POST'])
@jwt_required()
def add_story():
    user = get_jwt_identity()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Stories (user_id) VALUES (%s)", (user['user_id'],))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Story created successfully"}), 201

@app.route('/test-db')
def test_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SHOW TABLES;")
        tables = [t[0] for t in cur.fetchall()]
        cur.close()
        return {"connected": True, "tables": tables}
    except Exception as e:
        return {"connected": False, "error": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
