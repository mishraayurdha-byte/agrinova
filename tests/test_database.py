"""
====================================================
 AgriNova AI v2.0
 Database Tests
====================================================
"""

import pytest
from sqlalchemy import inspect

from database.models import (
    User,
    CropRecommendation,
    DiseaseHistory,
    WeatherHistory,
    FertilizerHistory,
    YieldHistory
)


# =====================================================
# Test Database Connection
# =====================================================

def test_database_connection(app, database):
    """
    Test database initialization.
    """

    with app.app_context():

        connection = database.engine.connect()

        assert connection is not None

        connection.close()


# =====================================================
# Test Database Tables
# =====================================================

def test_database_tables_exist(app):
    """
    Verify all required database tables exist.
    """

    expected_tables = [

        "users",

        "crop_recommendations",

        "disease_history",

        "weather_history",

        "fertilizer_history",

        "yield_history"

    ]

    with app.app_context():

        inspector = inspect(
            app.extensions["sqlalchemy"].engine
        )

        tables = inspector.get_table_names()

        for table in expected_tables:

            assert table in tables


# =====================================================
# Test Database Session
# =====================================================

def test_database_session(app, database):
    """
    Verify SQLAlchemy session operations.
    """

    with app.app_context():

        database.session.commit()

        assert True


# =====================================================
# Test Model Imports
# =====================================================

def test_models_loaded():
    """
    Verify all models are imported successfully.
    """

    assert User is not None

    assert CropRecommendation is not None

    assert DiseaseHistory is not None

    assert WeatherHistory is not None

    assert FertilizerHistory is not None

    assert YieldHistory is not None