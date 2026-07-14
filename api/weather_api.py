from flask import jsonify, request, Blueprint


weather_bp = Blueprint(
    "weather_bp",
    __name__,
    url_prefix="/api"
)

from services.weather_service import WeatherService
from services.weather_ai import WeatherAI
from database.models import WeatherHistory

@weather_bp.route("/weather", methods=["GET"])
def weather_analysis():
    """
    Live Weather Intelligence API
    Example:
    GET /api/weather?city=Delhi
    """

    city = request.args.get("city")

    if not city:
        return jsonify({
            "success": False,
            "message": "City parameter is required."
        }), 400

    weather = WeatherService.get_weather(city)

    if weather is None:
        return jsonify({
            "success": False,
            "message": "Unable to fetch weather data."
        }), 404

    advice = WeatherAI.generate_advice(weather)

    return jsonify({
        "success": True,
        "weather": weather,
        "farming_advice": advice
    }), 200


@weather_bp.route("/forecast", methods=["GET"])
def weather_forecast():
    """
    5-Day Weather Forecast
    Example:
    GET /api/forecast?city=Delhi
    """

    city = request.args.get("city")

    if not city:
        return jsonify({
            "success": False,
            "message": "City parameter is required."
        }), 400

    forecast = WeatherService.get_forecast(city)

    if forecast is None:
        return jsonify({
            "success": False,
            "message": "Unable to fetch forecast."
        }), 404

    return jsonify({
        "success": True,
        "forecast": forecast
    }), 200

#weather history
# ======================================================
# Weather History
# ======================================================

@weather_bp.route("/weather/history", methods=["GET"])
def weather_history():

    try:

        history = (
            WeatherHistory.query
            .order_by(
                WeatherHistory.created_at.desc()
            )
            .limit(20)
            .all()
        )


        return jsonify({

            "success": True,

            "history": [

                {

                    "city": item.city,

                    "temperature": item.temperature,

                    "humidity": item.humidity,

                    "pressure": item.pressure,

                    "wind_speed": item.wind_speed,

                    # Model field is condition
                    "weather": item.condition,

                    "description": item.description,

                    "icon": item.icon,

                    "created_at": item.created_at.strftime(
                        "%d-%m-%Y %H:%M"
                    )

                }

                for item in history

            ]

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500