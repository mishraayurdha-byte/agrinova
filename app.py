"""
==========================================================
AgriNova AI 

Main Flask Application

Handles:
- Web Interface
- API Blueprints
- Database Initialization
- AI Services
- Reports

==========================================================
"""

import os
import logging

from flask import Flask

from dotenv import load_dotenv

from config import Config
from database import db

from web import web_bp
from api import register_blueprints


# Load environment variables
load_dotenv()


# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ==========================================================
# Application Factory
# ==========================================================

def create_app():

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)


    # ======================================================
    # Database
    # ======================================================

    db.init_app(app)


    with app.app_context():

        try:
            db.create_all()
            logger.info("Database initialized successfully")

        except Exception as e:
            logger.error(
                f"Database initialization failed: {e}"
            )


    # ======================================================
    # Register Web Routes
    # ======================================================

    app.register_blueprint(
        web_bp
    )


    # ======================================================
    # Register API Routes
    # ======================================================

    register_blueprints(app)


    # ======================================================
    # Home Health Check
    # ======================================================

    @app.route("/health")
    def health():

        return {
            "status": "running",
            "application": "AgriNova AI "
        }


    return app



# ==========================================================
# Run Application
# ==========================================================

if __name__ == "__main__":

    app1 = create_app()

    app1.run(
    host="0.0.0.0",
    port=int(os.getenv("PORT", 5000)),
    debug=os.getenv("FLASK_DEBUG", "False").lower() == "true"
)
    
    app1 = create_app()

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=os.getenv("FLASK_DEBUG", "False").lower() == "true",
        use_reloader=False
    )