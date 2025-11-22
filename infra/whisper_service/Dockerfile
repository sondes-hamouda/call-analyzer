# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "app.py"]

