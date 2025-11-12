FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# копіюємо requirements
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# копіюємо увесь код з app/ (включно з my_project/)
COPY app ./app

# середовище
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app/my_project/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=8080

EXPOSE 8080

CMD ["python", "app/my_project/app.py"]
