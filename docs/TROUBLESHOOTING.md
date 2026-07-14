# AgriNova AI v2.0 Troubleshooting Guide

## Overview

This guide provides solutions to common issues encountered while installing, running, or deploying AgriNova AI v2.0.

---

# Installation Issues

## Python Not Found

### Problem

```text
python: command not found
```

or

```text
'python' is not recognized as an internal or external command.
```

### Solution

- Install Python 3.11 or later.
- Ensure Python is added to your system PATH.
- Verify the installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

## Virtual Environment Not Activated

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

If activation fails, recreate the environment:

```bash
python -m venv venv
```

---

## Dependency Installation Failed

### Problem

```text
ModuleNotFoundError
```

### Solution

Upgrade pip and reinstall dependencies:

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

# Database Issues

## SQLite Database Not Created

### Solution

Run:

```python
from app import create_app
from database import db

app = create_app()

with app.app_context():
    db.create_all()
```

Verify the database file:

```text
database/agrinova.db
```

---

## Database Locked

### Cause

SQLite allows only limited concurrent writes.

### Solution

- Stop other running instances of the application.
- Close any SQLite database viewers.
- Restart the application.

---

## Missing Tables

Verify that these tables exist:

```text
crop_predictions

disease_predictions

weather_history

irrigation_history

chat_history

reports
```

If missing, recreate the database.

---

# AI Model Issues

## Disease Model Not Found

### Error

```text
FileNotFoundError
```

### Solution

Verify:

```text
models/

disease_model.keras

disease_labels.json
```

---

## Yield Model Not Found

Verify:

```text
models/

yield_model.pkl

yield_scaler.pkl
```

---

## TensorFlow Errors

### Solution

Verify installation:

```bash
pip show tensorflow
```

Reinstall if necessary:

```bash
pip install tensorflow
```

---

## Scikit-learn Errors

Verify installation:

```bash
pip show scikit-learn
```

---

# Weather Module

## Weather Not Loading

### Possible Causes

- Invalid API key
- No internet connection
- OpenWeather service unavailable

### Solution

Verify:

```text
OPENWEATHER_API_KEY
```

inside:

```text
.env
```

---

## Invalid City

Verify that the entered city name is valid.

Example:

```text
Delhi

Mumbai

London

New York
```

---

# Disease Detection

## Upload Failed

Supported formats:

- JPG
- JPEG
- PNG

Verify:

- File size
- Image format
- Upload permissions

---

## Poor Prediction Accuracy

Recommended:

- Use clear images.
- Avoid blurry photos.
- Capture a single leaf.
- Ensure good lighting.

---

# Yield Prediction

## Unexpected Results

Verify that inputs are realistic.

Example:

```text
Rainfall

Temperature

Humidity

Soil Type
```

---

# Smart Irrigation

## Incorrect Recommendation

Check:

- Soil moisture value
- Temperature
- Humidity

Incorrect sensor values may produce inaccurate recommendations.

---

# Report Generation

## PDF Not Generated

Verify:

```bash
pip show reportlab
```

---

## Excel Not Generated

Verify:

```bash
pip show openpyxl
```

---

## CSV Export Failed

Ensure:

- Write permission to the `reports/` directory.
- Sufficient disk space.

---

# Chatbot

## No Response

Verify:

- Chatbot service is running.
- No exceptions in the application logs.

---

## Slow Response

Possible causes:

- Large AI model initialization.
- Limited CPU or memory.

Recommendation:

Load AI models once during application startup instead of on every request.

---

# Analytics

## Charts Not Displayed

Verify:

- Chart.js is loaded.
- Browser Developer Tools show no JavaScript errors.
- API endpoints return valid JSON.

---

# Docker Issues

## Docker Compose Build Failed

Run:

```bash
docker compose build --no-cache
```

---

## Container Not Starting

Inspect logs:

```bash
docker compose logs
```

---

## Restart Containers

```bash
docker compose restart
```

---

# Gunicorn Issues

## Workers Exiting

Check:

```text
logs/gunicorn_error.log
```

Increase timeout if AI inference takes longer than expected.

---

# Nginx Issues

## 502 Bad Gateway

Possible causes:

- Gunicorn is not running.
- Incorrect upstream configuration.
- Port mismatch.

Verify:

```text
Gunicorn -> 8000

Nginx -> 80
```

---

# Static Files Not Loading

Verify:

```text
static/

css/

js/

images/
```

Also confirm the Nginx `alias` paths in `nginx/default.conf`.

---

# Permission Issues

Ensure write access for:

```text
database/

logs/

reports/

uploads/
```

Linux example:

```bash
chmod -R 755 database logs reports uploads
```

---

# Performance Issues

## Slow Startup

Possible causes:

- TensorFlow model loading.
- Large AI models.
- Slow disk.

Recommendation:

Load AI models once during application initialization.

---

## High Memory Usage

Recommendations:

- Reduce Gunicorn workers.
- Optimize TensorFlow models.
- Remove unused dependencies.

---

# Browser Issues

Recommended browsers:

- Google Chrome
- Microsoft Edge
- Mozilla Firefox

If the UI behaves unexpectedly:

- Clear browser cache.
- Perform a hard refresh.
- Check the browser console for errors.

---

# Useful Commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python run.py
```

Run tests:

```bash
pytest
```

Run Docker:

```bash
docker compose up -d
```

View Docker logs:

```bash
docker compose logs -f
```

Stop Docker:

```bash
docker compose down
```

---

# Diagnostic Checklist

Before reporting an issue, verify:

- Python version is correct.
- Virtual environment is activated.
- Dependencies are installed.
- Database exists.
- AI models are available.
- OpenWeather API key is configured.
- Reports directory exists.
- Uploads directory exists.
- Docker containers are running (if using Docker).
- Application logs contain no critical errors.

---

# Getting Help

When reporting an issue, include:

- Operating System
- Python version
- Flask version
- Error message
- Full stack trace
- Relevant log entries
- Steps to reproduce the problem

Providing this information helps diagnose and resolve issues more quickly.

---

# Conclusion

Most issues can be resolved by verifying dependencies, configuration, file permissions, AI model availability, and log output. Following this guide should address the most common deployment and runtime problems encountered with AgriNova AI v2.0.