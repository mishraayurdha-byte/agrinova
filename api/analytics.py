"""
==========================================================
AgriNova AI
Analytics API

Provides:
- Dashboard statistics
- AI activity
- Farm analytics
- Chart data

==========================================================
"""

import logging

from flask import (
    Blueprint,
    jsonify,
    request
)

from database.repository import repository


logger = logging.getLogger(__name__)


# ==========================================================
# Blueprint
# ==========================================================

analytics_bp = Blueprint(

    "analytics",

    __name__,

    url_prefix="/api/analytics"

)



# ==========================================================
# Dashboard Overview
# ==========================================================

@analytics_bp.route(
    "/dashboard",
    methods=["GET"]
)
def dashboard():

    """
    Return dashboard statistics.
    """

    try:

        statistics = (

            repository.dashboard_statistics()

        )


        return jsonify({

            "success": True,

            "data": statistics

        })


    except Exception as error:


        logger.exception(error)


        return jsonify({

            "success": False,

            "message":
                "Unable to load dashboard data."

        }),500



# ==========================================================
# Recent AI Activity
# ==========================================================

@analytics_bp.route(
    "/recent",
    methods=["GET"]
)
def recent_activity():

    """
    Return recent AI predictions.
    """

    try:


        limit = int(

            request.args.get(
                "limit",
                10
            )

        )


        data = (

            repository.recent_predictions(

                limit

            )

        )


        return jsonify({

            "success": True,

            "count":
                len(data),

            "data":
                data

        })



    except Exception as error:


        logger.exception(error)


        return jsonify({

            "success": False,

            "message":
                "Unable to load AI activity."

        }),500



# ==========================================================
# Crop Analytics
# ==========================================================

@analytics_bp.route(
    "/crops",
    methods=["GET"]
)
def crop_statistics():

    """
    Return crop information.
    """

    try:


        crops = (

            repository.get_crops()

        )


        return jsonify({

            "success": True,

            "total_crops":
                len(crops),

            "data":
                crops

        })


    except Exception as error:


        logger.exception(error)


        return jsonify({

            "success": False,

            "message":
                "Unable to load crop data."

        }),500



# ==========================================================
# AI Health Status
# ==========================================================

@analytics_bp.route(
    "/health",
    methods=["GET"]
)
def ai_health():

    """
    System health information.
    """


    return jsonify({

        "success": True,

        "system":
            "AgriNova AI",

        "services": {


            "disease_detection":
                "active",


            "yield_prediction":
                "active",


            "smart_irrigation":
                "active",


            "weather_ai":
                "active"

        }

    })