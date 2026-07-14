# AgriNova AI v2.0 Installation Guide

## System Requirements

### Operating Systems

- Windows 10/11
- Ubuntu 22.04+
- macOS 13+

### Software

- Python 3.11+
- pip
- Git
- Docker Desktop (optional)
- Docker Compose (optional)

---

# Clone Repository

```bash
git clone https://github.com/yourusername/AgriNova_AI_v2.git

cd AgriNova_AI_v2
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv

venv\Scripts\activate
```

## Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

# Verify Installation

```bash
python --version

pip --version
```

---

# Configure Environment

Create a `.env` file in the project root.

Example:

```text
FLASK_ENV=development

SECRET_KEY=change-this-secret-key

OPENWEATHER_API_KEY=your_api_key

DATABASE_URL=sqlite:///database/agrinova.db
```

---

# Database Initialization

Create the SQLite database.

```bash
python
```

```python
from app import create_app
from database import db
app = create_app()

with app.app_context():
    db.create_all()
```

Alternatively, if your project uses Flask CLI:

```bash
flask db upgrade
```

---

# AI Models

Ensure the trained AI model files exist before starting the application.

Example structure:

```text
models/

├── disease_model.keras
├── disease_labels.json
├── yield_model.pkl
└── yield_scaler.pkl
```

> If the models are not present, run your AI training scripts before launching the application.

---

# Running the Application

Development mode:

```bash
python run.py
```

or

```bash
flask run
```

Default URL:

```text
http://127.0.0.1:5000
```

---

# Running with Docker

Build the containers:

```bash
docker compose build
```

Start the application:

```bash
docker compose up
```

Detached mode:

```bash
docker compose up -d
```

Stop the application:

```bash
docker compose down
```

---

# Project Directories

The following directories are created automatically if they do not exist:

```text
database/
uploads/
reports/
logs/
```

---

# Production Deployment

Production stack:

- Nginx
- Gunicorn
- Flask
- SQLite
- TensorFlow
- Scikit-learn

Start using Docker:

```bash
docker compose up -d --build
```

---

# Verify Installation

Open the application:

```text
http://localhost
```

Verify that the following pages are accessible:

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

---

# Troubleshooting

### ModuleNotFoundError

```bash
pip install -r requirements.txt
```

### Database Error

Delete the SQLite database (development only) and recreate it:

```bash
database/agrinova.db
```

Then run:

```python
db.create_all()
```

### OpenWeather API Issues

- Verify the API key in `.env`.
- Ensure outbound internet access is available.

### AI Model Loading Error

Check that all model files exist under the `models/` directory and that the filenames match the configuration.

---

# Support

If you encounter issues:

1. Check the application logs in the `logs/` directory.
2. Verify Docker container logs with:

```bash
docker compose logs
```

3. Confirm all dependencies are installed.