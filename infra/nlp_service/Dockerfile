# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Installer les dépendances système minimales
RUN apt-get update && apt-get install -y git

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5002

CMD ["python", "summarize.py"]

