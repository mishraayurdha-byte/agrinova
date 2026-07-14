from flask import render_template
from database.models import CropRecommendation, DiseaseHistory, FertilizerHistory, WeatherHistory, YieldHistory
from . import web_bp
from flask import send_file, Response
from services.export_service import ExportService
from services.report_service import ReportService
from services.chatbot_service import ChatbotService
from flask import request, jsonify
from services.analytics_service import AnalyticsService
from services.disease_service import DiseaseService
from werkzeug.utils import secure_filename
import os

@web_bp.route("/")
def home():
    return render_template("index.html")

from database.models import (
    CropRecommendation,
    WeatherHistory,
    DiseaseHistory,
    FertilizerHistory,
    YieldHistory
)
@web_bp.route("/dashboard")
def dashboard():

    statistics = {

        "crop_count": CropRecommendation.query.count(),

        "weather_count": WeatherHistory.query.count(),

        "disease_count": DiseaseHistory.query.count(),

        "fertilizer_count": FertilizerHistory.query.count(),

        "yield_count": YieldHistory.query.count(),

        "chat_count": 0

    }

    return render_template(
        "dashboard.html",
        statistics=statistics
    )


@web_bp.route("/crop")
def crop():
    return render_template("crop.html")


@web_bp.route("/weather")
def weather():
    return render_template("weather.html")


@web_bp.route("/api/disease/detect", methods=["GET", "POST"])
def disease():

    print(">>> Disease route called")

    if request.method == "POST":
        print(">>> POST request received")

        file = request.files.get("image")
        print(">>> File:", file)

    return render_template("disease.html")


@web_bp.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")


@web_bp.route("/yield")
def yield_page():
    return render_template("yield.html")

@web_bp.route("/analytics")
def analytics():

    summary = AnalyticsService.summary()

    recent_predictions = AnalyticsService.recent_predictions()


    return render_template(

        "analytics.html",

        summary=summary,

        recent_predictions=recent_predictions

    )



@web_bp.route("/reports")
def reports():

    statistics = ReportService.statistics()

    report_history = ReportService.recent_activity()

    return render_template(

        "reports.html",

        statistics=statistics,

        reports=report_history,

        ai_summary=statistics

    )

@web_bp.route("/chatbot")
def chatbot():

    chat_history = []

    return render_template(
        "chatbot.html",
        chat_history=chat_history
    )


@web_bp.route("/about")
def about():
    return render_template("about.html")


@web_bp.route("/contact")
def contact():
    return render_template("contact.html")


@web_bp.route("/irrigation")
def irrigation():
    return render_template("irrigation.html")


@web_bp.route("/api/chat", methods=["POST"])
def api_chat():

    data = request.get_json()

    message = data.get("message", "").strip()

   
    result = ChatbotService.ask(message)
    answer = result

    return jsonify({
        "status": "success",
        "answer": answer
    })