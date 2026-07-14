"""
==========================================================
AgriNova AI v2.0
Utility Helpers

Common helper functions used across the project.
==========================================================
"""

import os
import uuid
from pathlib import Path
from datetime import datetime
from werkzeug.utils import secure_filename
from config import Config
Config.SECRET_KEY


# ==========================================================
# File Helpers
# ==========================================================

def allowed_file(filename):
    """
    Check if uploaded file extension is allowed.
    """

    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return extension in config.ALLOWED_EXTENSIONS


def generate_filename(filename):
    """
    Generate a unique secure filename.
    """

    extension = filename.rsplit(".", 1)[1].lower()

    unique_name = uuid.uuid4().hex

    return secure_filename(
        f"{unique_name}.{extension}"
    )


# ==========================================================
# Directory Helpers
# ==========================================================

def ensure_directory(directory):
    """
    Create directory if it does not exist.
    """

    Path(directory).mkdir(
        parents=True,
        exist_ok=True
    )


# ==========================================================
# Date & Time
# ==========================================================

def current_timestamp():
    """
    Return current timestamp.
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


# ==========================================================
# Response Formatter
# ==========================================================

def format_response(
    success=True,
    message="",
    data=None
):
    """
    Standard API response format.
    """

    return {

        "success": success,

        "message": message,

        "timestamp": current_timestamp(),

        "data": data

    }


# ==========================================================
# File Size Formatter
# ==========================================================

def format_file_size(size):
    """
    Convert bytes into readable units.
    """

    units = [

        "B",

        "KB",

        "MB",

        "GB"

    ]

    value = float(size)

    for unit in units:

        if value < 1024:

            return f"{value:.2f} {unit}"

        value /= 1024

    return f"{value:.2f} TB"


# ==========================================================
# Random Identifier
# ==========================================================

def generate_id():
    """
    Generate random unique identifier.
    """

    return uuid.uuid4().hex


# ==========================================================
# File Path Helper
# ==========================================================

def upload_path(filename):
    """
    Return complete upload path.
    """

    ensure_directory(
        config.UPLOAD_FOLDER
    )

    return os.path.join(
        config.UPLOAD_FOLDER,
        filename
    )