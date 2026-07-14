from database.models import (
    CropRecommendation,
    WeatherHistory,
    DiseaseHistory,
    FertilizerHistory,
    YieldHistory
)


class DashboardService:

    def get_summary(self):

        return {

            "crop_count": CropRecommendation.query.count(),

            "weather_count": WeatherHistory.query.count(),

            "disease_count": DiseaseHistory.query.count(),

            "fertilizer_count": FertilizerHistory.query.count(),

            "yield_count": YieldHistory.query.count(),

            "chat_count": 0

        }