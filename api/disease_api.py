"""
==========================================================

AgriNova AI v2.0

Disease Detection API

Supports:
- Image Upload
- EfficientNetB0 Prediction
- Top 3 Predictions
- Disease History

==========================================================
"""

from pathlib import Path
import uuid

from flask import (
    Blueprint,
    jsonify,
    request
)

from werkzeug.utils import secure_filename

from services.disease_service import DiseaseService


# ==========================================================
# Blueprint
# ==========================================================

disease_bp = Blueprint(

    "disease",

    __name__,

    url_prefix="/disease"

)


service = DiseaseService()


# ==========================================================
# Upload Folder
# ==========================================================

UPLOAD_FOLDER = Path(

    "static/uploads"

)

UPLOAD_FOLDER.mkdir(

    parents=True,

    exist_ok=True

)


ALLOWED_EXTENSIONS = {

    "jpg",

    "jpeg",

    "png"

}


# ==========================================================
# Helpers
# ==========================================================

def allowed_file(filename):

    return (

        "." in filename

        and

        filename.rsplit(

            ".",

            1

        )[1].lower() in ALLOWED_EXTENSIONS

    )


# ==========================================================
# Predict Disease
# ==========================================================

@disease_bp.route(

    "/predict",

    methods=["POST"]

)

def predict():

    try:

        if "image" not in request.files:

            return jsonify({

                "success": False,

                "message": "No image uploaded."

            }), 400


        file = request.files["image"]


        if file.filename == "":

            return jsonify({

                "success": False,

                "message": "Please choose an image."

            }), 400


        if not allowed_file(file.filename):

            return jsonify({

                "success": False,

                "message": "Only JPG, JPEG and PNG images are allowed."

            }), 400


        extension = file.filename.rsplit(

            ".",

            1

        )[1].lower()


        filename = (

            f"{uuid.uuid4().hex}.{extension}"

        )


        filepath = UPLOAD_FOLDER / secure_filename(

            filename

        )


        file.save(

            filepath

        )


        result = service.predict(

            filepath

        )


        return jsonify(

            result

        )


    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500


# ==========================================================
# Health Check
# ==========================================================

@disease_bp.route(

    "/health",

    methods=["GET"]

)

def health():

    return jsonify({

        "success": True,

        "service": "Disease Detection API",

        "status": "Running"

    })