

from flask import jsonify, request, Blueprint


crop_bp = Blueprint(
    "crop_bp",
    __name__,
    url_prefix="/api"
)

# Get crop information
@crop_bp.route("/crop", methods=["GET"])
def get_crops():

    crops = [

        {
            "name": "Rice",
            "season": "Kharif",
            "soil": "Clay Loam",
            "water_requirement": "High",
            "duration": "120-150 days"
        },

        {
            "name": "Wheat",
            "season": "Rabi",
            "soil": "Loamy Soil",
            "water_requirement": "Medium",
            "duration": "120-140 days"
        },

        {
            "name": "Maize",
            "season": "Kharif/Rabi",
            "soil": "Well Drained Soil",
            "water_requirement": "Medium",
            "duration": "90-120 days"
        },

        {
            "name": "Potato",
            "season": "Rabi",
            "soil": "Sandy Loam",
            "water_requirement": "Medium",
            "duration": "90-110 days"
        }

    ]


    return jsonify({

        "success": True,

        "total": len(crops),

        "crops": crops

    }), 200



# Crop recommendation API
@crop_bp.route("/crop/recommend", methods=["POST"])
def crop_recommendation():

    try:

        data = request.get_json()


        required = [

            "soil_type",
            "rainfall",
            "temperature",
            "humidity"

        ]


        for field in required:

            if field not in data:

                return jsonify({

                    "success": False,

                    "message": f"{field} is required"

                }), 400



        soil = data["soil_type"].lower()

        rainfall = float(data["rainfall"])

        temperature = float(data["temperature"])



        # Simple AI rule-based recommendation
        if soil == "clay" and rainfall > 1000:

            recommended_crop = "Rice"


        elif temperature < 25 and rainfall < 800:

            recommended_crop = "Wheat"


        elif temperature >= 25 and rainfall >= 600:

            recommended_crop = "Maize"


        else:

            recommended_crop = "Vegetables"



        return jsonify({

            "success": True,

            "recommended_crop": recommended_crop,

            "input": data

        }), 200



    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500