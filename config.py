import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    # Flask secret key
    SECRET_KEY = "agrinova-secret-key"

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///"
        + os.path.join(BASE_DIR, "agrinova.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # Upload folder
    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "uploads"
    )



    # JSON settings
    JSON_SORT_KEYS = False

    # ==========================================
    # OpenWeather API
    # ==========================================

    OPENWEATHER_API_KEY = os.getenv(
        "WEATHER_API_KEY"
    )

    WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

    FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"