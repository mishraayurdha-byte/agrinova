import traceback

import requests

from config import Config
from database.models import WeatherHistory
from database import db


class WeatherService:


    @staticmethod
    def get_weather(city):
        """
        Fetch current weather from OpenWeather API.
        """

        if not Config.OPENWEATHER_API_KEY:

            raise ValueError(
                "OpenWeather API Key is missing."
            )


        params = {

            "q": city,

            "appid": Config.OPENWEATHER_API_KEY,

            "units": "metric"

        }
        print(
            "Weather Model Columns:",
            WeatherHistory.__table__.columns.keys()
        )

        try:

            response = requests.get(

                "https://api.openweathermap.org/data/2.5/weather",

                params=params,

                timeout=10

            )


            response.raise_for_status()


            data = response.json()



            weather = {

                "city": data["name"],

                "country": data["sys"]["country"],

                "temperature": data["main"]["temp"],                

                "humidity": data["main"]["humidity"],

                "pressure": data["main"]["pressure"],

                "wind_speed": data["wind"]["speed"],

                "condition": data["weather"][0]["main"],

                "description": data["weather"][0]["description"],

                "icon": data["weather"][0]["icon"]

            }



            # Save weather history

            WeatherService.save(weather)



            return weather



        except requests.exceptions.RequestException as e:


            print(
                f"Weather API Error: {e}"
            )


            return None





    @staticmethod
    def save(weather):

        """
        Save weather data into database.
        """

        try:


            record = WeatherHistory(


                city=weather["city"],


                temperature=weather["temperature"],


                humidity=weather["humidity"],


                pressure=weather["pressure"],


                wind_speed=weather["wind_speed"],


                condition=weather["condition"],


                description=weather.get(
                    "description"
                ),


                icon=weather.get(
                    "icon"
                )


            )


            db.session.add(record)


            db.session.commit()



            print(
                "Weather history saved successfully"
            )



        except Exception as e:


                    db.session.rollback()
                    import traceback
                    db.session.rollback()

                    traceback.print_exc()
                    print(
                        f"Database Error: {e}"
                    )






    @staticmethod
    def get_forecast(city):

        """
        Fetch 5-Day Weather Forecast.
        """

        params = {


            "q": city,


            "appid": Config.OPENWEATHER_API_KEY,


            "units": "metric"


        }



        try:


            response = requests.get(


                Config.FORECAST_URL,


                params=params,


                timeout=10


            )


            response.raise_for_status()


            data = response.json()



            return data



        except requests.exceptions.RequestException as e:


            print(
                f"Forecast API Error: {e}"
            )

               
            return None
        