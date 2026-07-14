"""
==========================================================
AgriNova AI v2.0
Recommendation Service

Responsible for:
- Fertilizer suggestions
- Irrigation decisions
- Crop advice
- Farming alerts

==========================================================
"""

import logging


logger = logging.getLogger(__name__)


class RecommendationService:
    """
    Farming Recommendation Intelligence Engine
    """


    # ======================================================
    # Fertilizer Recommendation
    # ======================================================

    def fertilizer_recommendation(
            self,
            soil_data,
            crop_name
    ):

        """
        Recommend fertilizer based on
        soil nutrient values.
        """


        nitrogen = soil_data.get(
            "nitrogen",
            0
        )

        phosphorus = soil_data.get(
            "phosphorus",
            0
        )

        potassium = soil_data.get(
            "potassium",
            0
        )


        recommendations = []


        if nitrogen < 50:

            recommendations.append(
                "Apply Nitrogen fertilizer (Urea)"
            )


        if phosphorus < 40:

            recommendations.append(
                "Apply Phosphorus fertilizer (DAP)"
            )


        if potassium < 50:

            recommendations.append(
                "Apply Potassium fertilizer (MOP)"
            )


        if not recommendations:

            recommendations.append(
                "Soil nutrients are balanced. Continue current practice."
            )


        return {


            "crop":

                crop_name,


            "recommendations":

                recommendations

        }



    # ======================================================
    # Smart Irrigation
    # ======================================================

    def irrigation_recommendation(
            self,
            soil_moisture,
            rainfall_prediction,
            temperature
    ):

        """
        AI based irrigation decision.
        """


        if rainfall_prediction > 70:


            return {


                "action":
                    "Do not irrigate",


                "reason":
                    "High rainfall probability detected.",


                "water_saved":
                    "High"


            }


        if soil_moisture < 35:


            return {


                "action":
                    "Start irrigation",


                "reason":
                    "Soil moisture is below required level.",


                "water_saved":
                    "Low"


            }


        if temperature > 35:


            return {


                "action":
                    "Light irrigation recommended",


                "reason":
                    "High temperature detected.",


                "water_saved":
                    "Medium"


            }



        return {


            "action":
                "No irrigation required",


            "reason":
                "Current soil condition is suitable.",


            "water_saved":
                "High"


        }



    # ======================================================
    # Crop Advice
    # ======================================================

    def crop_advice(
            self,
            crop_name,
            crop_stage
    ):

        """
        Provide crop stage advice.
        """


        advice = {


            "seedling":

            "Maintain moisture and monitor early growth.",


            "growing":

            "Monitor nutrients and protect from pests.",


            "flowering":

            "Ensure proper irrigation and nutrient supply.",


            "harvesting":

            "Prepare harvesting equipment and check weather."

        }



        return {


            "crop":
                crop_name,


            "stage":
                crop_stage,


            "advice":
                advice.get(

                    crop_stage.lower(),

                    "Continue regular crop monitoring."

                )

        }



    # ======================================================
    # Weather Risk Analysis
    # ======================================================

    def weather_risk_analysis(
            self,
            temperature,
            humidity,
            rainfall
    ):

        """
        Analyze farming risks from weather.
        """


        alerts = []


        if temperature > 38:

            alerts.append(

                "High temperature risk. Check irrigation."

            )


        if humidity > 85:

            alerts.append(

                "High humidity may increase disease risk."

            )


        if rainfall > 100:

            alerts.append(

                "Heavy rainfall risk. Protect crops."

            )


        if not alerts:

            alerts.append(

                "Weather conditions are favorable."

            )


        return {


            "alerts":

                alerts

        }



    # ======================================================
    # Complete Farm Recommendation
    # ======================================================

    def generate_farm_report(
            self,
            farm_data
    ):

        """
        Generate complete AI farming report.
        """


        return {


            "fertilizer":

                self.fertilizer_recommendation(

                    farm_data.get(
                        "soil",
                        {}
                    ),

                    farm_data.get(
                        "crop",
                        "Unknown"
                    )

                ),


            "irrigation":

                self.irrigation_recommendation(

                    farm_data.get(
                        "soil_moisture",
                        50
                    ),

                    farm_data.get(
                        "rainfall",
                        0
                    ),

                    farm_data.get(
                        "temperature",
                        30
                    )

                ),


            "weather":

                self.weather_risk_analysis(

                    farm_data.get(
                        "temperature",
                        30
                    ),

                    farm_data.get(
                        "humidity",
                        60
                    ),

                    farm_data.get(
                        "rainfall",
                        0
                    )

                )

        }



# ==========================================================
# Singleton Object
# ==========================================================

recommendation_service = RecommendationService()