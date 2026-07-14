"""
==========================================================
AgriNova AI v2.0
Validation Utilities

Validation helpers used across APIs and services.
==========================================================
"""

import re

from config import Config


# ==========================================================
# Email Validation
# ==========================================================

EMAIL_PATTERN = re.compile(

    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

)


def validate_email(email):
    """
    Validate email address.
    """

    if not email:

        return False

    return EMAIL_PATTERN.match(email) is not None


# ==========================================================
# Phone Validation
# ==========================================================

PHONE_PATTERN = re.compile(

    r"^[0-9]{10}$"

)


def validate_phone(phone):
    """
    Validate 10-digit phone number.
    """

    if not phone:

        return False

    return PHONE_PATTERN.match(phone) is not None


# ==========================================================
# Crop Name
# ==========================================================

SUPPORTED_CROPS = {

    "rice",
    "wheat",
    "maize",
    "corn",
    "cotton",
    "soybean",
    "potato",
    "tomato",
    "onion",
    "sugarcane"

}


def validate_crop_name(crop_name):
    """
    Validate supported crop.
    """

    if not crop_name:

        return False

    return crop_name.lower() in SUPPORTED_CROPS


# ==========================================================
# Temperature
# ==========================================================

def validate_temperature(value):
    """
    Acceptable range:
    -20°C to 60°C
    """

    try:

        value = float(value)

    except Exception:

        return False

    return -20 <= value <= 60


# ==========================================================
# Soil Moisture
# ==========================================================

def validate_soil_moisture(value):
    """
    Percentage: 0–100
    """

    try:

        value = float(value)

    except Exception:

        return False

    return 0 <= value <= 100


# ==========================================================
# Humidity
# ==========================================================

def validate_humidity(value):
    """
    Percentage: 0–100
    """

    try:

        value = float(value)

    except Exception:

        return False

    return 0 <= value <= 100


# ==========================================================
# Rainfall
# ==========================================================

def validate_rainfall(value):
    """
    Rainfall (mm)
    """

    try:

        value = float(value)

    except Exception:

        return False

    return 0 <= value <= 5000


# ==========================================================
# Image File
# ==========================================================

def validate_image(filename):
    """
    Validate uploaded image extension.
    """

    if not filename:

        return False

    if "." not in filename:

        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return extension in config.ALLOWED_EXTENSIONS


# ==========================================================
# Yield Prediction Input
# ==========================================================

def validate_yield_input(data):
    """
    Validate required fields for
    crop yield prediction.
    """

    required_fields = [

        "temperature",
        "humidity",
        "rainfall",
        "soil_moisture"

    ]

    for field in required_fields:

        if field not in data:

            return False

    return (

        validate_temperature(data["temperature"])
        and
        validate_humidity(data["humidity"])
        and
        validate_rainfall(data["rainfall"])
        and
        validate_soil_moisture(data["soil_moisture"])

    )