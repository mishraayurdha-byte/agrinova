from flask import jsonify

from api import api_bp
from services.analytics_service import AnalyticsService


@api_bp.route("/analytics", methods=["GET"])
def analytics():

    summary = AnalyticsService.summary()

    return jsonify({

        "success": True,
        "summary": summary

    })


@api_bp.route("/analytics/latest-weather", methods=["GET"])
def latest_weather():

    weather = AnalyticsService.latest_weather()

    if weather is None:

        return jsonify({

            "success": False

        }), 404

    return jsonify({

        "success": True,

        "weather": {

            "city": weather.city,
            "temperature": weather.temperature,
            "humidity": weather.humidity,
            "condition": weather.condition

        }

    })


@api_bp.route("/analytics/recent-predictions")
def recent_predictions():

    rows = AnalyticsService.recent_predictions()

    data = []

    for row in rows:

        data.append({

            "crop": row.crop,
            "prediction": row.prediction,
            "temperature": row.temperature,
            "humidity": row.humidity

        })

    return jsonify({

        "success": True,
        "data": data

    })