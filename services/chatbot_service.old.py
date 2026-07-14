"""
==========================================================

AgriNova AI v2.0

AI Farming Chatbot Service

Supports:
- Crop Recommendation
- Disease Guidance
- Fertilizer Advice
- Irrigation Advice
- Weather Suggestions
- General Farming Questions

==========================================================
"""

import re

from database import db

from  models.chat_history import ChatHistory

from database.disease_data import DISEASE_DATABASE


class ChatbotService:


    def __init__(self):

        self.responses = {

            "greeting":

                "Hello 👋 I'm AgriNova AI. How can I help you today?",

            "unknown":

                "Sorry, I couldn't understand your question. Please ask about crops, diseases, fertilizer, irrigation, weather or farming."

        }


    # ======================================================
    # Main Chat Function
    # ======================================================

    def get_response(

        self,

        message

    ):

        question = message.lower().strip()


        if any(

            word in question

            for word in [

                "hello",

                "hi",

                "hey"

            ]

        ):

            answer = self.responses["greeting"]


        elif "crop" in question:

            answer = self.crop_advice(question)


        elif any(

            word in question

            for word in [

                "disease",

                "blight",

                "virus",

                "spot",

                "rust",

                "mold"

            ]

        ):

            answer = self.disease_advice(question)


        elif any(

            word in question

            for word in [

                "fertilizer",

                "npk",

                "nitrogen",

                "phosphorus",

                "potassium"

            ]

        ):

            answer = self.fertilizer_advice(question)


        elif any(

            word in question

            for word in [

                "water",

                "irrigation",

                "soil moisture"

            ]

        ):

            answer = self.irrigation_advice(question)


        elif any(

            word in question

            for word in [

                "weather",

                "rain",

                "temperature"

            ]

        ):

            answer = self.weather_advice(question)


        else:

            answer = self.responses["unknown"]


        history = ChatHistory(

            question=message,

            answer=answer

        )

        db.session.add(history)

        db.session.commit()


        return {

            "success": True,

            "question": message,

            "answer": answer

        }


    # ======================================================
    # Crop Recommendation
    # ======================================================

    def crop_advice(

        self,

        question

    ):

        return (

            "For accurate crop recommendation, please use the Crop Recommendation module and provide N, P, K, temperature, humidity, pH and rainfall."

        )
        # ======================================================
    # Disease Advice
    # ======================================================

    def disease_advice(

        self,

        question

    ):

        question = question.lower()


        # Search disease database

        for disease_name, info in DISEASE_DATABASE.items():

            disease_key = disease_name.lower().replace("_", " ")

            if disease_key in question:

                return (

                    f"🦠 Disease: {disease_name}\n\n"

                    f"📖 Description:\n"

                    f"{info.get('description','Not Available')}\n\n"

                    f"🔍 Symptoms:\n"

                    f"{info.get('symptoms','Not Available')}\n\n"

                    f"💊 Treatment:\n"

                    f"{info.get('treatment','Not Available')}\n\n"

                    f"🛡 Prevention:\n"

                    f"{info.get('prevention','Not Available')}"

                )


        return (

            "Please mention the disease name.\n\n"

            "Examples:\n"

            "- Tomato Early Blight\n"

            "- Tomato Late Blight\n"

            "- Apple Scab\n"

            "- Potato Early Blight\n"

            "- Corn Rust"

        )


    # ======================================================
    # Fertilizer Advice
    # ======================================================

    def fertilizer_advice(

        self,

        question

    ):

        return (

            "🌱 Fertilizer Recommendation\n\n"

            "• Apply fertilizer only after soil testing.\n"

            "• Maintain balanced NPK levels.\n"

            "• Organic compost improves soil health.\n"

            "• Avoid over-fertilization.\n"

            "• Use the Fertilizer Recommendation module for AI-based advice."

        )


    # ======================================================
    # Irrigation Advice
    # ======================================================

    def irrigation_advice(

        self,

        question

    ):

        return (

            "💧 Irrigation Guidance\n\n"

            "• Irrigate early morning or evening.\n"

            "• Maintain proper soil moisture.\n"

            "• Avoid waterlogging.\n"

            "• Prefer drip irrigation for water efficiency.\n"

            "• Use the Irrigation module for AI recommendations."

        )


    # ======================================================
    # Weather Advice
    # ======================================================

    def weather_advice(

        self,

        question

    ):

        return (

            "🌦 Weather Guidance\n\n"

            "• Monitor rainfall forecasts.\n"

            "• Avoid fertilizer spraying before rain.\n"

            "• Protect crops during extreme temperatures.\n"

            "• Use the Weather Intelligence module for live weather updates and AI recommendations."

        )