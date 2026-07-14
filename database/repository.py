"""
==========================================================
AgriNova AI v2.0
Database Repository Layer

Responsible for:
- Saving AI results
- Reading farm data
- Dashboard statistics
- Database operations

==========================================================
"""

import json
import logging

from database.db import db


logger = logging.getLogger(__name__)


class Repository:
    """
    Central database operation layer.
    """


    # ======================================================
    # Disease Detection
    # ======================================================

    def save_disease_prediction(
            self,
            data
    ):

        """
        Save disease detection result.
        """

        query = """

        INSERT INTO disease_detection

        (
            crop_name,
            image_path,
            disease_name,
            confidence,
            treatment
        )

        VALUES (?, ?, ?, ?, ?)

        """


        return db.execute(

            query,

            (

                data.get(
                    "crop_name",
                    "Unknown"
                ),

                data.get(
                    "image_path"
                ),

                data.get(
                    "disease"
                ),

                data.get(
                    "confidence"
                ),

                data.get(
                    "treatment"
                )

            )

        )



    # ======================================================
    # Yield Prediction
    # ======================================================

    def save_yield_prediction(
            self,
            input_data,
            result
    ):

        """
        Store yield prediction.
        """

        query = """

        INSERT INTO ai_predictions

        (
            prediction_type,
            input_data,
            result,
            confidence
        )

        VALUES (?, ?, ?, ?)

        """


        return db.execute(

            query,

            (

                "Yield Prediction",

                json.dumps(
                    input_data
                ),

                json.dumps(
                    result
                ),

                result.get(
                    "confidence",
                    0
                )

            )

        )



    # ======================================================
    # Irrigation
    # ======================================================

    def save_irrigation(
            self,
            data
    ):

        """
        Save irrigation recommendation.
        """

        query = """

        INSERT INTO irrigation

        (
            crop_id,
            soil_moisture,
            water_used,
            ai_recommendation,
            irrigation_status
        )

        VALUES (?, ?, ?, ?, ?)

        """


        return db.execute(

            query,

            (

                data.get(
                    "crop_id",
                    1
                ),

                data.get(
                    "soil_moisture",
                    0
                ),

                data.get(
                    "water_used",
                    0
                ),

                data.get(
                    "recommendation"
                ),

                data.get(
                    "status"
                )

            )

        )



    # ======================================================
    # Weather Storage
    # ======================================================

    def save_weather(
            self,
            weather
    ):

        """
        Store weather information.
        """

        query = """

        INSERT INTO weather

        (
            temperature,
            humidity,
            rainfall,
            condition
        )

        VALUES (?, ?, ?, ?)

        """


        return db.execute(

            query,

            (

                weather.get(
                    "temperature"
                ),

                weather.get(
                    "humidity"
                ),

                weather.get(
                    "rainfall"
                ),

                weather.get(
                    "condition"
                )

            )

        )



    # ======================================================
    # Dashboard Statistics
    # ======================================================

    def dashboard_statistics(self):

        """
        Generate dashboard numbers.
        """

        disease_count = db.fetch_one(

            """
            SELECT COUNT(*) AS total
            FROM disease_detection
            """

        )


        prediction_count = db.fetch_one(

            """
            SELECT COUNT(*) AS total
            FROM ai_predictions
            """

        )


        irrigation_count = db.fetch_one(

            """
            SELECT COUNT(*) AS total
            FROM irrigation
            """

        )


        return {


            "disease_scans":

                disease_count["total"],


            "ai_predictions":

                prediction_count["total"],


            "irrigation_records":

                irrigation_count["total"]

        }



    # ======================================================
    # Recent Predictions
    # ======================================================

    def recent_predictions(
            self,
            limit=10
    ):

        """
        Get recent AI predictions.
        """

        rows = db.fetch_all(

            """

            SELECT *

            FROM ai_predictions

            ORDER BY created_at DESC

            LIMIT ?

            """,

            (

                limit,

            )

        )


        return [

            dict(row)

            for row in rows

        ]



    # ======================================================
    # Crop List
    # ======================================================

    def get_crops(self):

        """
        Return crop records.
        """

        rows = db.fetch_all(

            """

            SELECT *

            FROM crops

            ORDER BY id DESC

            """

        )


        return [

            dict(row)

            for row in rows

        ]



# ==========================================================
# Singleton Repository
# ==========================================================

repository = Repository()