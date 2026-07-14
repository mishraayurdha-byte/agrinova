"""
database/init_db.py

Database initialization for AgriNova AI v2.0
"""

import logging

from database import db

logger = logging.getLogger(__name__)


def initialize_database(app):
    """
    Create all database tables.
    """

    with app.app_context():
        try:
            # Import all models so SQLAlchemy registers them
            import models

            db.create_all()

            logger.info("AgriNova AI database initialized successfully.")

        except Exception as e:
            logger.exception("Database initialization failed.")
            raise e