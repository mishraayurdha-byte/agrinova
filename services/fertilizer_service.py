"""
==========================================================
AgriNova AI v2.0

Fertilizer Recommendation Service

==========================================================
"""


class FertilizerService:

    def recommend(
        self,
        crop,
        soil_type,
        nitrogen,
        phosphorus,
        potassium
    ):

        fertilizers = []
        advice = []

        # ==========================================
        # Nitrogen Analysis
        # ==========================================

        if nitrogen < 50:

            nitrogen_status = "Low"

            fertilizers.append("Urea")

            advice.append(
                "Nitrogen level is low. Apply Urea in split doses for better leaf and stem growth."
            )

        elif nitrogen <= 100:

            nitrogen_status = "Optimal"

        else:

            nitrogen_status = "High"

            advice.append(
                "Nitrogen is already high. Avoid additional nitrogen fertilizer."
            )

        # ==========================================
        # Phosphorus Analysis
        # ==========================================

        if phosphorus < 40:

            phosphorus_status = "Low"

            fertilizers.append("DAP")

            advice.append(
                "Phosphorus is low. Apply DAP to encourage strong root development."
            )

        elif phosphorus <= 80:

            phosphorus_status = "Optimal"

        else:

            phosphorus_status = "High"

            advice.append(
                "Phosphorus is already sufficient. Avoid excess phosphorus application."
            )

        # ==========================================
        # Potassium Analysis
        # ==========================================

        if potassium < 40:

            potassium_status = "Low"

            fertilizers.append("MOP")

            advice.append(
                "Potassium is low. Apply MOP to improve crop quality and disease resistance."
            )

        elif potassium <= 80:

            potassium_status = "Optimal"

        else:

            potassium_status = "High"

            advice.append(
                "Potassium level is high. Additional potassium is not required."
            )

        # ==========================================
        # Balanced Soil
        # ==========================================

        if len(fertilizers) == 0:

            fertilizers.append("Balanced NPK Fertilizer")

            advice.append(
                "Your soil nutrient levels are balanced. Continue regular soil monitoring."
            )

        # Remove duplicates

        fertilizers = list(dict.fromkeys(fertilizers))

        # ==========================================
        # Soil Health
        # ==========================================

        if (
            nitrogen_status == "Optimal"
            and phosphorus_status == "Optimal"
            and potassium_status == "Optimal"
        ):

            soil_health = "Excellent"

        elif (
            nitrogen_status == "Low"
            or phosphorus_status == "Low"
            or potassium_status == "Low"
        ):

            soil_health = "Needs Improvement"

        else:

            soil_health = "Good"

        # ==========================================
        # General Advice
        # ==========================================

        general_tips = [

            "Apply fertilizers after soil testing whenever possible.",

            "Irrigate the field after fertilizer application.",

            "Avoid applying excessive fertilizer as it may reduce yield.",

            "Use organic compost regularly to improve soil fertility."

        ]

        # ==========================================
        # Response
        # ==========================================

        return {

            "crop": crop,

            "soil_type": soil_type,

            "soil_health": soil_health,

            "nitrogen_status": nitrogen_status,

            "phosphorus_status": phosphorus_status,

            "potassium_status": potassium_status,

            "recommended_fertilizer": fertilizers,

            "advice": advice,

            "general_tips": general_tips

        }