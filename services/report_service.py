"""
==========================================================

AgriNova AI v2.0

Report Service

==========================================================
"""

from database.models import (

    CropRecommendation,

    DiseaseHistory,

    FertilizerHistory,

    WeatherHistory,

    YieldHistory

)

from models.chat_history import ChatHistory
from models.report import Report
from models.irrigation_history import IrrigationHistory

class ReportService:


    # ======================================================
    # Dashboard Statistics
    # ======================================================

    @staticmethod
    def statistics():

        return {

            "crop_count":

                CropRecommendation.query.count(),

            "disease_count":

                DiseaseHistory.query.count(),

            "fertilizer_count":

                FertilizerHistory.query.count(),

            "weather_count":

                WeatherHistory.query.count(),

            "yield_count":

                YieldHistory.query.count(),

            "irrigation_count":

                IrrigationHistory.query.count(),

            "chat_count":

                ChatHistory.query.count(),

            "report_count":

                Report.query.count()

        }


    # ======================================================
    # Recent Disease Predictions
    # ======================================================

    @staticmethod
    def recent_diseases(limit=10):

        return DiseaseHistory.query.order_by(

            DiseaseHistory.created_at.desc()

        ).limit(

            limit

        ).all()


    # ======================================================
    # Recent Crop Predictions
    # ======================================================

    @staticmethod
    def recent_crops(limit=10):

        return CropRecommendation.query.order_by(

            CropRecommendation.created_at.desc()

        ).limit(

            limit

        ).all()


    # ======================================================
    # Recent Fertilizer Predictions
    # ======================================================

    @staticmethod
    def recent_fertilizers(limit=10):

        return FertilizerHistory.query.order_by(

            FertilizerHistory.created_at.desc()

        ).limit(

            limit

        ).all()


    # ======================================================
    # Recent Yield Predictions
    # ======================================================

    @staticmethod
    def recent_yields(limit=10):

        return YieldHistory.query.order_by(

            YieldHistory.created_at.desc()

        ).limit(

            limit

        ).all()


    # ======================================================
    # Recent Weather Queries
    # ======================================================

    @staticmethod
    def recent_weather(limit=10):

        return WeatherHistory.query.order_by(

            WeatherHistory.created_at.desc()

        ).limit(

            limit

        ).all()


    # ======================================================
    # Recent Irrigation Predictions
    # ======================================================

    @staticmethod
    def recent_irrigation(limit=10):

        return IrrigationHistory.query.order_by(

            IrrigationHistory.created_at.desc()

        ).limit(

            limit

        ).all()


    # ======================================================
    # Recent Chats
    # ======================================================

    @staticmethod
    def recent_chats(limit=10):

        return ChatHistory.query.order_by(

            ChatHistory.created_at.desc()

        ).limit(

            limit

        ).all()


    # ======================================================
    # Recent Activities
    # ======================================================

    @staticmethod
    def recent_activity():

        return {

            "diseases":

                ReportService.recent_diseases(5),

            "crops":

                ReportService.recent_crops(5),

            "fertilizers":

                ReportService.recent_fertilizers(5),

            "weather":

                ReportService.recent_weather(5),

            "yield":

                ReportService.recent_yields(5),

            "irrigation":

                ReportService.recent_irrigation(5),

            "chats":

                ReportService.recent_chats(5)

        }