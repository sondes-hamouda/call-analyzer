# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Installer les dépendances nécessaires


COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg
RUN pip install --no-cache-dir --timeout=200 --retries=10 -r requirements.txt


COPY . .

EXPOSE 5001

CMD ["python", "app.py"]

