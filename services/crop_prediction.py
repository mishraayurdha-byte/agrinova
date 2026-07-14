"""
==========================================================
AgriNova AI v2.0

Crop Prediction Service

Handles:
- Crop recommendation prediction
- ML model loading
- Feature processing
- Prediction response

==========================================================
"""

import os
import logging
import joblib
import numpy as np

logger = logging.getLogger(__name__)


class CropPrediction:


    MODEL_PATH = os.path.join(
        "models",
        "crop_recommendation_model.pkl"
    )


    def __init__(self):

        self.model = None

        self.load_model()



    # ======================================================
    # Load ML Model
    # ======================================================

    def load_model(self):

        try:

            if os.path.exists(
                self.MODEL_PATH
            ):

                self.model = joblib.load(
                    self.MODEL_PATH
                )

                logger.info(
                    "Crop prediction model loaded"
                )

            else:

                logger.warning(
                    "Crop model not found, using rule engine"
                )


        except Exception as e:

            logger.error(
                f"Model loading error: {e}"
            )



    # ======================================================
    # Predict Crop
    # ======================================================

    def predict(
        self,
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        rainfall
    ):


        try:


            features = np.array([

                nitrogen,
                phosphorus,
                potassium,
                temperature,
                humidity,
                rainfall

            ]).reshape(1, -1)



            # ML Prediction

            if self.model:


                prediction = self.model.predict(
                    features
                )


                return {

                    "crop":
                        str(prediction[0]),

                    "method":
                        "ML Model"

                }



            # Fallback Rule Engine

            return self.rule_prediction(
                temperature,
                rainfall,
                humidity
            )



        except Exception as e:


            logger.error(
                f"Crop prediction failed: {e}"
            )


            return {

                "crop": None,

                "error": str(e)

            }



    # ======================================================
    # Rule Based Prediction
    # ======================================================

    def rule_prediction(
        self,
        temperature,
        rainfall,
        humidity
    ):


        if rainfall > 200:

            crop = "Rice"


        elif temperature < 25:

            crop = "Wheat"


        elif humidity > 60:

            crop = "Maize"


        else:

            crop = "Cotton"



        return {

            "crop": crop,

            "method":
                "Rule Engine"

        }



# ==========================================================
# Service Instance
# ==========================================================

crop_prediction_service = CropPrediction()