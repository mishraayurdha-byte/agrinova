# ====================================================
# AgriNova AI v2.0
# Production Dockerfile
# ====================================================

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# ----------------------------------------------------
# System Dependencies
# ----------------------------------------------------

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libgl1 \
    libglib2.0-0 \
    libjpeg-dev \
    zlib1g-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------------------------------
# Python Dependencies
# ----------------------------------------------------

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# ----------------------------------------------------
# Application
# ----------------------------------------------------

COPY . .

# ----------------------------------------------------
# Runtime Directories
# ----------------------------------------------------

RUN mkdir -p \
    reports \
    uploads \
    logs

# ----------------------------------------------------
# Flask
# ----------------------------------------------------

ENV FLASK_APP=run.py

ENV FLASK_ENV=production

EXPOSE 8000

# ----------------------------------------------------
# Gunicorn
# ----------------------------------------------------

CMD [
    "gunicorn",
    "-c",
    "gunicorn.conf.py",
    "run:app"
]