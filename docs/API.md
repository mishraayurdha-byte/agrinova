# AgriNova AI v2.0 API Documentation

## Overview

AgriNova AI v2.0 provides RESTful APIs for AI-powered agricultural services including disease detection, yield prediction, smart irrigation, weather information, chatbot assistance, analytics, and report generation.

**Base URL (Development)**

```text
http://localhost:5000
```

**Base URL (Docker)**

```text
http://localhost
```

---

# Response Format

## Success

```json
{
    "success": true,
    "message": "Operation completed successfully"
}
```

## Error

```json
{
    "success": false,
    "message": "Description of the error"
}
```

---

# Disease Detection

## Detect Crop Disease

### Endpoint

```http
POST /api/disease/detect
```

### Content Type

```text
multipart/form-data
```

### Request

| Field | Type | Required |
|--------|------|----------|
| image | File | Yes |

### Success Response

```json
{
    "success": true,
    "disease": "Healthy Leaf",
    "confidence": 98.45,
    "recommendation": "No treatment required"
}
```

---

# Yield Prediction

## Predict Crop Yield

### Endpoint

```http
POST /api/yield/predict
```

### Request

```json
{
    "crop": "Rice",
    "area": 2,
    "rainfall": 120,
    "temperature": 28,
    "humidity": 70,
    "soil": "Loamy"
}
```

### Success Response

```json
{
    "success": true,
    "crop": "Rice",
    "predicted_yield": 6.2,
    "accuracy": "95%",
    "recommendation": "Maintain soil nutrients"
}
```

---

# Smart Irrigation

## Calculate Irrigation Recommendation

### Endpoint

```http
POST /api/irrigation
```

### Request

```json
{
    "soil_moisture": 22,
    "temperature": 31,
    "humidity": 42
}
```

### Success Response

```json
{
    "success": true,
    "status": "ON",
    "score": 82,
    "water_amount": "25 Liters",
    "duration": "35 Minutes",
    "message": "Low soil moisture detected"
}
```

---

# Weather

## Current Weather

### Endpoint

```http
GET /api/weather?city=Delhi
```

### Success Response

```json
{
    "success": true,
    "city": "Delhi",
    "temperature": 31,
    "humidity": 58,
    "pressure": 1011,
    "wind_speed": 12,
    "condition": "Cloudy",
    "description": "Partly cloudy"
}
```

---

# AI Chatbot

## Ask Farming Questions

### Endpoint

```http
POST /api/chatbot
```

### Request

```json
{
    "message": "How can I improve rice yield?"
}
```

### Success Response

```json
{
    "success": true,
    "answer": "Maintain balanced fertilizer application and proper irrigation."
}
```

---

# Analytics

## Dashboard Analytics

### Endpoint

```http
GET /api/analytics
```

### Success Response

```json
{
    "summary": {
        "yield_predictions": 120,
        "disease_predictions": 85,
        "weather_records": 300,
        "chat_messages": 75
    },
    "yield": {
        "labels": ["Jan", "Feb", "Mar"],
        "values": [4.2, 5.1, 6.0]
    },
    "disease": {
        "labels": ["Healthy", "Blight"],
        "values": [80, 20]
    },
    "weather": {
        "labels": ["Mon", "Tue", "Wed"],
        "values": [31, 30, 29]
    },
    "irrigation": {
        "labels": ["ON", "OFF"],
        "values": [60, 40]
    }
}
```

---

# Reports

## Generate Report

### Endpoint

```http
POST /api/reports/generate
```

### Request

```json
{
    "type": "yield",
    "format": "pdf"
}
```

Supported formats:

- pdf
- xlsx
- csv

### Success Response

```json
{
    "success": true,
    "file": "reports/agrinova_yield_20260710_103500.pdf"
}
```

---

## Download Report

### Endpoint

```http
GET /api/reports/download/<filename>
```

Example:

```http
GET /api/reports/download/agrinova_yield_20260710_103500.pdf
```

---

# HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 201 | Resource Created |
| 400 | Bad Request |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# Notes

- All API responses are JSON except file downloads.
- Authentication is intentionally **disabled** in AgriNova AI v2.0.
- The frontend communicates with these endpoints using the JavaScript modules in `static/js/`.
- Uploaded images should be sent using `multipart/form-data`.