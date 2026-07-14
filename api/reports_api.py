"""
==========================================================

AgriNova AI v2.0

Reports API

Handles:
- Dashboard Statistics
- Recent Activities
- Disease History
- Crop History
- Weather History
- Yield History
- Fertilizer History
- Irrigation History
- Chat History

==========================================================
"""

from flask import (

    Blueprint,

    jsonify

)

from services.report_service import ReportService


# ==========================================================
# Blueprint
# ==========================================================

reports_bp = Blueprint(

    "reports",

    __name__,

    url_prefix="/reports"

)


# ==========================================================
# Dashboard Statistics
# ==========================================================

@reports_bp.route(

    "/statistics",

    methods=["GET"]

)

def statistics():

    return jsonify(

        ReportService.statistics()

    )


# ==========================================================
# Recent Activity
# ==========================================================

@reports_bp.route(

    "/activity",

    methods=["GET"]

)

def activity():

    data = ReportService.recent_activity()

    return jsonify(

        {

            "success": True,

            "data": {

                "diseases": [

                    item.to_dict()

                    for item in data["diseases"]

                ],

                "crops": [

                    item.to_dict()

                    for item in data["crops"]

                ],

                "fertilizers": [

                    item.to_dict()

                    for item in data["fertilizers"]

                ],

                "weather": [

                    item.to_dict()

                    for item in data["weather"]

                ],

                "yield": [

                    item.to_dict()

                    for item in data["yield"]

                ],

                "irrigation": [

                    item.to_dict()

                    for item in data["irrigation"]

                ],

                "chats": [

                    item.to_dict()

                    for item in data["chats"]

                ]

            }

        }

    )


# ==========================================================
# Disease History
# ==========================================================

@reports_bp.route(

    "/diseases",

    methods=["GET"]

)

def diseases():

    return jsonify(

        [

            item.to_dict()

            for item in ReportService.recent_diseases(100)

        ]

    )


# ==========================================================
# Crop History
# ==========================================================

@reports_bp.route(

    "/crops",

    methods=["GET"]

)

def crops():

    return jsonify(

        [

            item.to_dict()

            for item in ReportService.recent_crops(100)

        ]

    )


# ==========================================================
# Fertilizer History
# ==========================================================

@reports_bp.route(

    "/fertilizers",

    methods=["GET"]

)

def fertilizers():

    return jsonify(

        [

            item.to_dict()

            for item in ReportService.recent_fertilizers(100)

        ]

    )


# ==========================================================
# Weather History
# ==========================================================

@reports_bp.route(

    "/weather",

    methods=["GET"]

)

def weather():

    return jsonify(

        [

            item.to_dict()

            for item in ReportService.recent_weather(100)

        ]

    )


# ==========================================================
# Yield History
# ==========================================================

@reports_bp.route(

    "/yield",

    methods=["GET"]

)

def yield_history():

    return jsonify(

        [

            item.to_dict()

            for item in ReportService.recent_yields(100)

        ]

    )


# ==========================================================
# Irrigation History
# ==========================================================

@reports_bp.route(

    "/irrigation",

    methods=["GET"]

)

def irrigation():

    return jsonify(

        [

            item.to_dict()

            for item in ReportService.recent_irrigation(100)

        ]

    )


# ==========================================================
# Chat History
# ==========================================================

@reports_bp.route(

    "/chat",

    methods=["GET"]

)

def chat():

    return jsonify(

        [

            item.to_dict()

            for item in ReportService.recent_chats(100)

        ]

    )


# ==========================================================
# Health Check
# ==========================================================

@reports_bp.route(

    "/health",

    methods=["GET"]

)

def health():

    return jsonify(

        {

            "success": True,

            "service": "Reports API",

            "status": "Running"

        }

    )