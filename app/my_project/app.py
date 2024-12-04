import os
from flask import Flask, current_app
from flask_mysqldb import MySQL
from auth.route import user_bp, story_bp, media_bp
app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'lab4'

app.config['MYSQL_SSL_DISABLED'] = True

app.mysql = mysql

app.register_blueprint(user_bp)
app.register_blueprint(story_bp)
app.register_blueprint(media_bp)

if __name__ == '__main__':
    app.run(debug=True)
