"""
==========================================================
AgriNova AI v2.0
Application Constants
==========================================================
"""

# ==========================================================
# Application
# ==========================================================

APP_NAME = "AgriNova AI"

APP_VERSION = "2.0.0"

APP_TAGLINE = "Growing Tomorrow with Smart Farming"

APP_DESCRIPTION = (
    "Artificial Intelligence Powered Smart Farming Platform"
)


# ==========================================================
# Upload Settings
# ==========================================================

ALLOWED_IMAGE_EXTENSIONS = {

    "jpg",
    "jpeg",
    "png"

}

MAX_IMAGE_SIZE = 5 * 1024 * 1024      # 5 MB


# ==========================================================
# AI Configuration
# ==========================================================

AI_CONFIDENCE_THRESHOLD = 0.85

MODEL_IMAGE_WIDTH = 224

MODEL_IMAGE_HEIGHT = 224

MODEL_CHANNELS = 3


# ==========================================================
# Supported Crops
# ==========================================================

SUPPORTED_CROPS = [

    "Rice",
    "Wheat",
    "Maize",
    "Corn",
    "Cotton",
    "Potato",
    "Tomato",
    "Onion",
    "Soybean",
    "Sugarcane"

]


# ==========================================================
# Disease Classes
# ==========================================================

DISEASE_CLASSES = [

    "Healthy",

    "Leaf Blight",

    "Early Blight",

    "Late Blight",

    "Leaf Spot",

    "Rust",

    "Powdery Mildew"

]


# ==========================================================
# Irrigation
# ==========================================================

LOW_SOIL_MOISTURE = 35

MEDIUM_SOIL_MOISTURE = 60

HIGH_SOIL_MOISTURE = 85


# ==========================================================
# Weather Defaults
# ==========================================================

DEFAULT_CITY = "New Delhi"

DEFAULT_COUNTRY = "India"

DEFAULT_TEMPERATURE = 25.0

DEFAULT_HUMIDITY = 65

DEFAULT_RAINFALL = 0


# ==========================================================
# Dashboard
# ==========================================================

DEFAULT_DASHBOARD_LIMIT = 10

MAX_RECENT_RECORDS = 100


# ==========================================================
# Report Formats
# ==========================================================

SUPPORTED_REPORT_FORMATS = [

    "pdf",

    "xlsx",

    "csv"

]


# ==========================================================
# API Response Messages
# ==========================================================

SUCCESS = "Operation completed successfully."

FAILED = "Operation failed."

INVALID_INPUT = "Invalid input."

MODEL_NOT_FOUND = "AI model not found."

FILE_NOT_SUPPORTED = "Unsupported file format."

SERVER_ERROR = "Internal server error."


# ==========================================================
# Logging
# ==========================================================

LOG_FORMAT = (

    "%(asctime)s | %(levelname)s | %(message)s"

)


LOG_LEVEL = "INFO"


# ==========================================================
# Theme Colors
# ==========================================================

PRIMARY_COLOR = "#198754"

SECONDARY_COLOR = "#0d6efd"

WARNING_COLOR = "#ffc107"

DANGER_COLOR = "#dc3545"

SUCCESS_COLOR = "#198754"