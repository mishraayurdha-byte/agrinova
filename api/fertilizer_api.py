from flask import jsonify, request, Blueprint


from services.fertilizer_service import FertilizerService


fertilizer_bp = Blueprint(
    "fertilizer_bp",
    __name__,
    url_prefix="/api"
)

service = FertilizerService()


# ==========================================================
# Fertilizer Recommendation API
# ==========================================================

@fertilizer_bp.route("/fertilizer/recommend", methods=["POST"])
def fertilizer_recommendation():

    try:

        data = request.get_json()

        if not data:

            return jsonify({

                "success": False,

                "message": "No input data received."

            }), 400


        required = [

            "crop",
            "soil_type",
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


        result = service.recommend(

            crop=data["crop"],

            soil_type=data["soil_type"],

            nitrogen=float(data["nitrogen"]),

            phosphorus=float(data["phosphorus"]),

            potassium=float(data["potassium"])

        )


        return jsonify({

            "success": True,

            "result": result

        }), 200


    except ValueError:

        return jsonify({

            "success": False,

            "message": "Nitrogen, Phosphorus and Potassium must be numeric."

        }), 400


    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500