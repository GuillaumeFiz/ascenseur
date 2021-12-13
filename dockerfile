
FROM python:3.7-slim-bullseye

# # Création d'un user pour éviter l'utilisation via root
RUN adduser --disabled-password --gecos '' appuser
USER appuser
WORKDIR /app

ENV PATH="/home/appuser/.local/bin:${PATH}"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR src
