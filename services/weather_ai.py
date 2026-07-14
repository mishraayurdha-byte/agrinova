class WeatherAI:

    @staticmethod
    def generate_advice(weather):
        """
        Generate AI farming recommendations based on weather conditions.
        """

        advice = []

        temperature = weather.get("temperature", 0)
        humidity = weather.get("humidity", 0)
        wind_speed = weather.get("wind_speed", 0)
        condition = weather.get("condition", "").lower()

        # Temperature Advice
        if temperature >= 38:
            advice.append("🔥 Extreme heat detected. Increase irrigation and avoid midday farming activities.")
        elif temperature >= 32:
            advice.append("☀️ Hot weather. Irrigate crops early morning or late evening.")
        elif temperature <= 10:
            advice.append("❄️ Low temperature. Protect seedlings and sensitive crops from cold stress.")

        # Humidity Advice
        if humidity >= 85:
            advice.append("💧 High humidity may promote fungal diseases. Monitor crops regularly.")
        elif humidity <= 30:
            advice.append("🌾 Low humidity detected. Increase irrigation frequency if required.")

        # Wind Advice
        if wind_speed >= 10:
            advice.append("💨 Strong winds expected. Avoid pesticide spraying and support young plants.")

        # Weather Condition Advice
        if "rain" in condition:
            advice.append("🌧️ Rain expected. Delay irrigation and ensure proper drainage.")
        elif "drizzle" in condition:
            advice.append("🌦️ Light rain detected. Monitor soil moisture before watering.")
        elif "thunderstorm" in condition:
            advice.append("⛈️ Thunderstorm alert. Avoid field work until weather improves.")
        elif "clear" in condition:
            advice.append("☀️ Clear weather. Suitable for harvesting, spraying and field operations.")
        elif "cloud" in condition:
            advice.append("☁️ Cloudy weather. Good conditions for transplanting crops.")
        elif "mist" in condition or "fog" in condition:
            advice.append("🌫️ Foggy conditions. Monitor crops for fungal infections.")
        elif "snow" in condition:
            advice.append("❄️ Snowfall detected. Protect crops from frost damage.")

        # Default Advice
        if not advice:
            advice.append("✅ Weather conditions are normal. Continue regular farming practices.")

        return advice