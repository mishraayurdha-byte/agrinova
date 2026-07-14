# AgriNova AI v2.0 Developer Guide

## Introduction

This guide is intended for developers who want to understand, maintain, or extend AgriNova AI v2.0.

The project follows a modular architecture based on Flask, SQLAlchemy, TensorFlow, and Scikit-learn.

---

# Technology Stack

## Backend

- Python 3.11+
- Flask
- SQLAlchemy
- SQLite

## Artificial Intelligence

- TensorFlow (Disease Detection)
- Scikit-learn (Yield Prediction)

## Frontend

- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- Chart.js

## Deployment

- Docker
- Gunicorn
- Nginx

---

# Project Architecture

```text
Client Browser
       │
       ▼
     Nginx
       │
       ▼
   Gunicorn
       │
       ▼
 Flask Application
       │
 ┌─────┼────────────────────────────┐
 │     │            │               │
 ▼     ▼            ▼               ▼
API  Services      AI Models     Database
 │                  │               │
 └──────────────────┴───────────────┘
                   │
                   ▼
                SQLite
```

---

# Directory Structure

```text
AgriNova_AI_v2/
│
├── ai/
├── api/
├── database/
├── docs/
├── models/
├── services/
├── static/
├── templates/
├── tests/
├── uploads/
├── utils/
│
├── app.py
├── run.py
├── config.py
├── extensions.py
├── requirements.txt
└── Dockerfile
```

---

# Application Entry Point

The application starts from:

```text
run.py
```

Example:

```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

Production uses:

- Gunicorn
- Nginx

---

# Application Factory

The project uses the Flask Application Factory pattern.

Responsibilities:

- Initialize Flask
- Load configuration
- Register blueprints
- Initialize extensions
- Configure error handlers

---

# API Layer

The `api/` directory contains REST API endpoints.

```text
api/

analytics_api.py
chatbot_api.py
disease_api.py
irrigation_api.py
reports_api.py
weather_api.py
yield_api.py
```

Each API module is responsible for:

- Request validation
- Calling service layer
- Returning JSON responses
- Error handling

Business logic should **not** be implemented inside API routes.

---

# Service Layer

Business logic is implemented inside:

```text
services/
```

Modules:

- analytics_service.py
- chatbot_service.py
- disease_service.py
- irrigation_service.py
- report_service.py
- weather_service.py
- yield_service.py

Responsibilities:

- AI model execution
- Database operations
- External API communication
- Data processing
- Report generation

---

# Database Layer

SQLAlchemy models are located in:

```text
models/
```

Current database tables:

- crop_predictions
- disease_predictions
- weather_history
- irrigation_history
- chat_history
- reports

All database access should be performed through SQLAlchemy ORM.

---

# AI Models

## Disease Detection

Framework:

```text
TensorFlow
```

Expected model files:

```text
models/

disease_model.keras

disease_labels.json
```

Responsibilities:

- Load trained model
- Preprocess image
- Predict disease
- Return confidence score

---

## Yield Prediction

Framework:

```text
Scikit-learn
```

Expected files:

```text
models/

yield_model.pkl

yield_scaler.pkl
```

Responsibilities:

- Scale input data
- Predict yield
- Return recommendation

---

# Frontend

Templates:

```text
templates/
```

Static files:

```text
static/
```

CSS:

```text
static/css/
```

JavaScript:

```text
static/js/
```

Images:

```text
static/images/
```

Bootstrap 5 is used throughout the application.

---

# Charts

Chart.js powers:

- Dashboard
- Analytics
- Reports

Recommended practice:

- Keep chart configuration in dedicated JavaScript files.
- Avoid inline JavaScript inside templates.

---

# Reports

Supported formats:

- PDF
- Excel (XLSX)
- CSV

Generated reports are stored in:

```text
reports/
```

---

# Weather Integration

Provider:

OpenWeather API

Configuration:

```text
.env
```

Required variable:

```text
OPENWEATHER_API_KEY
```

The Weather Service handles:

- API requests
- Error handling
- Data formatting
- Database storage

---

# Error Handling

Each API should return consistent JSON.

Example:

```json
{
    "success": false,
    "message": "Invalid input"
}
```

Recommended status codes:

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad Request |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# Logging

Logs should be stored in:

```text
logs/
```

Recommended log files:

```text
application.log

gunicorn_access.log

gunicorn_error.log
```

---

# Testing

Framework:

```text
pytest
```

Run all tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=.
```

---

# Docker

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

Production stack:

- Flask
- Gunicorn
- Nginx

---

# Coding Standards

Recommended guidelines:

- Follow PEP 8.
- Use descriptive function names.
- Keep functions focused on a single responsibility.
- Separate API logic from business logic.
- Add docstrings for public classes and functions.
- Use type hints where practical.

---

# Extending the Project

To add a new feature:

1. Create a database model if required.
2. Implement business logic in `services/`.
3. Add API endpoints in `api/`.
4. Create templates if a UI is needed.
5. Add JavaScript and CSS assets.
6. Write tests.
7. Update documentation.

---

# Security Notes

Current project configuration:

- Authentication removed
- No user management
- No admin panel

For production deployments with multiple users, consider adding:

- User authentication
- Role-based authorization
- CSRF protection
- Rate limiting
- HTTPS
- Secure session management

---

# Performance Recommendations

- Cache weather responses where appropriate.
- Load AI models once during application startup.
- Optimize uploaded image sizes before inference.
- Use pagination for large datasets.
- Enable browser caching for static assets.
- Monitor Gunicorn worker usage in production.

---

# Contribution Workflow

1. Create a feature branch.
2. Implement changes.
3. Run formatting and tests.
4. Update documentation if required.
5. Submit a pull request for review.

---

# Summary

AgriNova AI v2.0 follows a clean, modular architecture that separates presentation, business logic, AI inference, and data persistence. This structure simplifies maintenance, testing, 
and future enhancements while supporting production deployment with Docker, Gunicorn, and Nginx.