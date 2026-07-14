# AgriNova AI v2.0 Project Structure

## Overview

AgriNova AI v2.0 follows a modular architecture that separates the application into independent layers for maintainability, scalability, and ease of development.

---

# Root Directory

```text
AgriNova_AI_v2/
│
├── ai/
├── api/
├── config/
├── database/
├── docs/
├── logs/
├── migrations/
├── models/
├── reports/
├── routes/
├── services/
├── static/
├── templates/
├── tests/
├── uploads/
├── utils/
│
├── app.py
├── run.py
├── extensions.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── gunicorn.conf.py
├── .dockerignore
├── .gitignore
└── README.md
```

---

# AI Module

```text
ai/
│
├── disease_detection/
│   ├── train.py
│   ├── predict.py
│   ├── preprocess.py
│   └── model.keras
│
└── yield_prediction/
    ├── train.py
    ├── predict.py
    ├── preprocess.py
    ├── model.pkl
    └── scaler.pkl
```

Purpose:

- TensorFlow disease detection
- Scikit-learn yield prediction
- Model training
- Model inference

---

# API Layer

```text
api/
│
├── analytics_api.py
├── chatbot_api.py
├── disease_api.py
├── irrigation_api.py
├── reports_api.py
├── weather_api.py
└── yield_api.py
```

Purpose:

- REST API endpoints
- Request validation
- JSON responses
- Service integration

---

# Services

```text
services/
│
├── analytics_service.py
├── chatbot_service.py
├── disease_service.py
├── irrigation_service.py
├── report_service.py
├── weather_service.py
└── yield_service.py
```

Purpose:

- Business logic
- AI model execution
- Database operations
- External API integration

---

# Database Models

```text
models/
│
├── chat_history.py
├── crop_prediction.py
├── disease_prediction.py
├── irrigation_history.py
├── report.py
├── weather_history.py
└── __init__.py
```

Database Tables

- crop_predictions
- disease_predictions
- weather_history
- irrigation_history
- chat_history
- reports

---

# Templates

```text
templates/
│
├── base.html
├── index.html
├── dashboard.html
├── disease.html
├── yield.html
├── irrigation.html
├── weather.html
├── chatbot.html
├── analytics.html
├── reports.html
├── about.html
├── contact.html
│
├── components/
│   ├── navbar.html
│   ├── sidebar.html
│   ├── footer.html
│   ├── loader.html
│   └── toast.html
│
└── errors/
    ├── 404.html
    └── 500.html
```

---

# Static Files

```text
static/
│
├── css/
│   ├── style.css
│   ├── dashboard.css
│   ├── disease.css
│   ├── chatbot.css
│   ├── analytics.css
│   ├── reports.css
│   └── responsive.css
│
├── js/
│   ├── app.js
│   ├── analytics.js
│   ├── chatbot.js
│   ├── disease.js
│   ├── irrigation.js
│   ├── reports.js
│   ├── weather.js
│   └── yield.js
│
├── images/
│
└── uploads/
```

---

# Utilities

```text
utils/
│
├── constants.py
├── helpers.py
├── validators.py
├── file_handler.py
├── logger.py
└── response.py
```

---

# Documentation

```text
docs/
│
├── API.md
├── CHANGELOG.md
├── DEVELOPER_GUIDE.md
├── DEPLOYMENT.md
├── INSTALLATION.md
├── LICENSE.md
├── PROJECT_STRUCTURE.md
├── README.md
├── TROUBLESHOOTING.md
└── USER_GUIDE.md
```

---

# Testing

```text
tests/
│
├── conftest.py
├── test_chatbot.py
├── test_database.py
├── test_disease.py
├── test_irrigation.py
├── test_reports.py
├── test_weather.py
└── test_yield.py
```

---

# Generated Data

```text
database/
│
└── agrinova.db
```

```text
reports/
```

```text
uploads/
```

```text
logs/
```

---

# Docker Deployment

```text
Dockerfile

docker-compose.yml

gunicorn.conf.py

nginx/
│
└── default.conf
```

---

# Navigation

The application contains the following modules:

- Home
- Dashboard
- Disease Detection
- Yield Prediction
- Smart Irrigation
- Weather
- AI Chatbot
- Analytics
- Reports
- About
- Contact

Authentication has been intentionally removed.

- No Login
- No Register
- No Admin
- No Settings

---

# Technology Stack

## Backend

- Flask
- SQLAlchemy
- SQLite

## Artificial Intelligence

- TensorFlow
- Scikit-learn

## Frontend

- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- Chart.js

## External Services

- OpenWeather API

## Reporting

- ReportLab
- OpenPyXL
- CSV

## Deployment

- Docker
- Gunicorn
- Nginx

---

# Architecture

```text
Browser
      │
      ▼
Nginx Reverse Proxy
      │
      ▼
Gunicorn
      │
      ▼
Flask Application
      │
 ┌────┼──────────────┐
 │    │              │
 ▼    ▼              ▼
AI  Services     Database
 │                 │
 └──────────┬──────┘
            ▼
        SQLite
```

---

# Design Principles

- Modular Architecture
- Service-Oriented Design
- RESTful APIs
- Separation of Concerns
- Responsive User Interface
- Production-Ready Deployment
- Easy Maintenance
- Scalable Structure