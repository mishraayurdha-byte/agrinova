from database.models import (
    
    
    WeatherHistory,
    
    
)

from models.crop_prediction_model import CropPrediction
from models.chat_history import ChatHistory
from models.disease_prediction import DiseasePrediction
from models.irrigation_history import IrrigationHistory

class AnalyticsService:

    @staticmethod
    def summary():

        return {

            "yield_predictions":
                CropPrediction.query.count(),

            "disease_predictions":
                DiseasePrediction.query.count(),

            "weather_records":
                WeatherHistory.query.count(),

            "irrigation_records":
                IrrigationHistory.query.count(),

            "chat_messages":
                ChatHistory.query.count()
        }

    @staticmethod
    def latest_weather():

        return WeatherHistory.query.order_by(
            WeatherHistory.id.desc()
        ).first()

    @staticmethod
    def recent_predictions(limit=10):

        return CropPrediction.query.order_by(
            CropPrediction.id.desc()
        ).limit(limit).all()