from flask import jsonify, request, Blueprint


yield_bp = Blueprint(
    "yield_bp",
    __name__,
    url_prefix="/api"
)


from services.yield_service import YieldService


@yield_bp.route("/yield", methods=["POST"])
def yield_prediction():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "Request body is required."
            }), 400


        required = [
            "crop",
            "rainfall",
            "temperature",
            "humidity",
            "nitrogen",
            "phosphorus",
            "potassium"
        ]


        for field in required:

            if field not in data:

                return jsonify({

                    "success": False,
                    "message": f"{field} is required."

                }), 400



        features = [

            float(data["rainfall"]),
            float(data["temperature"]),
            float(data["humidity"]),
            float(data["nitrogen"]),
            float(data["phosphorus"]),
            float(data["potassium"])

        ]



        service = YieldService()


        prediction = service.predict(features)



        save_data = {

            "crop": data["crop"],

            "rainfall": float(data["rainfall"]),

            "temperature": float(data["temperature"]),

            "humidity": float(data["humidity"]),

            "nitrogen": float(data["nitrogen"]),

            "phosphorus": float(data["phosphorus"]),

            "potassium": float(data["potassium"]),

            "prediction": prediction

        }



        service.save(save_data)



        return jsonify({

            "success": True,

            "message": "Yield prediction successful",

            "prediction": prediction

        }), 200



    except ValueError as e:

        return jsonify({

            "success": False,

            "message": "Invalid numeric value provided.",

            "error": str(e)

        }), 400



    except Exception as e:

        return jsonify({

            "success": False,

            "message": "Server error",

            "error": str(e)

        }), 500