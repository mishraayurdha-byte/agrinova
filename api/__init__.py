"""
==========================================================
AgriNova AI 

API Blueprint Manager

Registers:
- Crop API
- Weather API
- Yield API
- Fertilizer API
- Irrigation API
- Reports API
- Disease API
- Chatbot API

==========================================================
"""


from flask import Blueprint



# ==========================================================
# Main API Blueprint
# ==========================================================

api_bp = Blueprint(

    "api",

    __name__,

    url_prefix="/api"

)



# ==========================================================
# Register All APIs
# ==========================================================

def register_blueprints(app):


    from .crop_api import crop_bp
    from .weather_api import weather_bp
    from .yield_api import yield_bp
    from .fertilizer_api import fertilizer_bp
    from .irrigation_api import irrigation_bp
    from .reports_api import reports_bp
    from .disease_api import disease_bp
    from .chat_api import chat_bp



    # Register API blueprints

    app.register_blueprint(
        crop_bp
    )


    app.register_blueprint(
        weather_bp
    )


    app.register_blueprint(
        yield_bp
    )


    app.register_blueprint(
        fertilizer_bp
    )


    app.register_blueprint(
        irrigation_bp
    )


    app.register_blueprint(
        reports_bp
    )


    app.register_blueprint(
        disease_bp
    )


    app.register_blueprint(
        chat_bp
    )