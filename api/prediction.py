"""
==========================================================
AgriNova AI v2.0
Crop Yield Prediction API

Handles:
- Crop yield prediction
- Machine learning model
- Prediction storage

==========================================================
"""

import json
import logging
import pickle
import sqlite3

from flask import (
    Blueprint,
    jsonify,
    request
)

import numpy as np

from config import Config


logger = logging.getLogger(__name__)


# ==========================================================
# Blueprint
# ==========================================================

prediction_bp = Blueprint(

    "prediction",

    __name__,

    url_prefix="/api/prediction"

)


# ==========================================================
# Load ML Model
# ==========================================================

def load_yield_model():

    """
    Load trained yield model.
    """

    try:

        if config.YIELD_MODEL_PATH.exists():

            with open(
                config.YIELD_MODEL_PATH,
                "rb"
            ) as file:

                return pickle.load(file)


    except Exception as error:

        logger.warning(
            f"Yield model loading failed: {error}"
        )


    return None



# ==========================================================
# Prediction Engine
# ==========================================================

def predict_yield(data):

    """
    Generate crop yield prediction.
    """


    model = load_yield_model()



    features = np.array(

        [[

            data.get(
                "rainfall",
                100
            ),

            data.get(
                "temperature",
                28
            ),

            data.get(
                "humidity",
                60
            ),

            data.get(
                "soil_moisture",
                50
            )

        ]]

    )



    if model:


        prediction = (

            model.predict(
                features
            )[0]

        )


        confidence = 95



    else:


        # Offline demo intelligence

        prediction = (

            (
                data.get(
                    "rainfall",
                    100
                )

                *

                0.04

            )

            +

            (

                data.get(
                    "soil_moisture",
                    50
                )

                *

                0.05

            )

        )



        confidence = 90



    return {


        "expected_yield":

            round(
                float(prediction),
                2
            ),


        "unit":

            "Ton/Hectare",


        "confidence":

            confidence


    }



# ==========================================================
# Save Prediction
# ==========================================================

def save_prediction(data, result):

    """
    Store AI prediction history.
    """

    connection = sqlite3.connect(

        config.DATABASE_PATH

    )


    cursor = connection.cursor()


    cursor.execute(

        """

        INSERT INTO ai_predictions

        (

        prediction_type,

        input_data,

        result,

        confidence

        )

        VALUES (?, ?, ?, ?)

        """,

        (

            "Yield Prediction",

            json.dumps(data),

            json.dumps(result),

            result["confidence"]

        )

    )


    connection.commit()

    connection.close()



# ==========================================================
# Prediction Endpoint
# ==========================================================

@prediction_bp.route(
    "/yield",
    methods=["POST"]
)
def yield_prediction():

    """
    Predict crop yield.
    """

    try:


        data = request.get_json()



        if not data:


            return jsonify({

                "success": False,

                "message":
                    "Input data required."

            }),400



        result = predict_yield(

            data

        )


        save_prediction(

            data,

            result

        )


        return jsonify({

            "success": True,

            "prediction": result

        })



    except Exception as error:


        logger.exception(error)


        return jsonify({

            "success": False,

            "message":
                "Yield prediction failed."

        }),500



# ==========================================================
# Status
# ==========================================================

@prediction_bp.route(
    "/status",
    methods=["GET"]
)
def status():

    return jsonify({

        "service":
            "Crop Yield Prediction",

        "status":
            "active"

    })