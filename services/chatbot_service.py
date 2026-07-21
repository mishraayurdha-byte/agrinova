"""
==========================================================
AgriNova AI
AI Chatbot Service (Google Gemini)
==========================================================
"""

import os
import google.generativeai as genai


class ChatbotService:

    model = None
    current_key = None
    current_model = None
    current_key_index = 0

    MODELS = [
        "gemini-2.5-flash",
        "gemini-3.1-flash-lite",
        "gemini-2.5-pro",
        "gemini-2.0-flash"
    ]

    @classmethod
    def initialize(cls):

        api_keys = [
            key.strip()
            for key in os.getenv("GEMINI_API_KEYS", "").split(",")
            if key.strip()
        ]

        if not api_keys:
            raise Exception("GEMINI_API_KEYS not found in environment.")

        last_error = None

        # Start from the current key index
        for i in range(cls.current_key_index, len(api_keys)):

            api_key = api_keys[i]

            print(f"\nTrying API Key {i + 1}/{len(api_keys)}")

            genai.configure(api_key=api_key)

            for model_name in cls.MODELS:

                try:

                    print(f"Trying Model: {model_name}")

                    model = genai.GenerativeModel(model_name)

                    # Test model
                    model.generate_content("Hello")

                    cls.model = model
                    cls.current_key = api_key
                    cls.current_model = model_name
                    cls.current_key_index = i

                    print(f"Connected using {model_name}")

                    return

                except Exception as e:

                    last_error = e
                    error = str(e).lower()

                    print(f"{model_name} failed: {e}")

                    # Model unavailable → try next model
                    if (
                        "404" in error
                        or "not found" in error
                        or "no longer available" in error
                    ):
                        continue

                    # Quota exhausted → switch API key
                    if (
                        "429" in error
                        or "quota" in error
                        or "resource_exhausted" in error
                    ):
                        print("Quota exceeded. Trying next API key...")
                        break

                    # Other error → try next model
                    continue

        raise Exception(f"No working Gemini model/API key found.\n{last_error}")

    @classmethod
    def ask(cls, message):

        if cls.model is None:
            cls.initialize()

        prompt = f"""
You are AgriNova AI, an expert agricultural assistant.

Instructions:
1. Detect the language of the user's question.
2. Reply in the SAME language.
3. Keep answers short, practical and farmer-friendly.
4. Use bullet points whenever helpful.
5. Answer ONLY agriculture-related questions.
6. If the question is unrelated to agriculture, politely explain that AgriNova AI focuses on farming topics.

User Question:
{message}

Give a clear answer in the SAME language.
"""

        try:

            response = cls.model.generate_content(prompt)

            return response.text

        except Exception as e:

            error = str(e).lower()

            # Quota exceeded → move to next key
            if (
                "429" in error
                or "quota" in error
                or "resource_exhausted" in error
            ):

                print("Current API key quota exceeded.")
                print("Switching to next API key...")

                cls.current_key_index += 1
                cls.model = None

                cls.initialize()

                response = cls.model.generate_content(prompt)

                return response.text

            # Model removed → retry with another model
            if (
                "404" in error
                or "not found" in error
                or "no longer available" in error
            ):

                print("Current model unavailable.")
                print("Searching for another model...")

                cls.model = None

                cls.initialize()

                response = cls.model.generate_content(prompt)

                return response.text

            raise