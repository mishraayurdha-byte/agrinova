"""
==========================================================
AgriNova AI v2.0
AI Chatbot Service (Google Gemini)
==========================================================
"""

import os

import google.generativeai as genai


class ChatbotService:

    model = None

    @classmethod
    def initialize(cls):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise Exception("GEMINI_API_KEY not found.")

        genai.configure(api_key=api_key)

        cls.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    @classmethod
    def ask(cls, message):

        if cls.model is None:
            cls.initialize()

        prompt = f"""
You are AgriNova AI.

You are an expert agricultural assistant.

Answer only farming-related questions.

Topics include:
- Crop Recommendation
- Irrigation
- Fertilizer
- Plant Diseases
- Soil
- Weather
- Yield Prediction
- Organic Farming

Question:
{message}

Give a clear answer in simple English.
"""

        response = cls.model.generate_content(prompt)

        return response.text