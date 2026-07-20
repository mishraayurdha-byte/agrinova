# ======================================================
# AgriNova AI 
# Smart Irrigation API
# ======================================================

from flask import jsonify, request, Blueprint


from services.irrigation_service import IrrigationService


irrigation_bp = Blueprint(
    "irrigation_bp",
    __name__,
    url_prefix="/api"
)

# ======================================================
# Irrigation Prediction
# ======================================================

@irrigation_bp.route("/irrigation", methods=["POST"])
def irrigation():

    try:

        data = request.get_json()


        soil = float(
            data["soil_moisture"]
        )

        temp = float(
            data["temperature"]
        )

        humidity = float(
            data["humidity"]
        )


        # AI Calculation

        result = IrrigationService.calculate(

            soil,

            temp,

            humidity

        )


        # Save complete result

        IrrigationService.save(
            result
        )


        return jsonify({

            "success": True,

            "result": result

        })


    except Exception as e:


        return jsonify({

            "success": False,

            "message": str(e)

        }), 500





# ======================================================
# Irrigation History
# ======================================================

@irrigation_bp.route(
    "/irrigation/history",
    methods=["GET"]
)
def irrigation_history():

    try:


        history = IrrigationService.get_history()


        return jsonify({

            "success": True,

            "history": history

        })


    except Exception as e:


        return jsonify({

            "success": False,

            "message": str(e)

        }), 500