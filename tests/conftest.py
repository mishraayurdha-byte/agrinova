"""
====================================================
 AgriNova AI v2.0
 Pytest Configuration
====================================================
"""


import pytest


from app import create_app

from database import db





@pytest.fixture
def app():

    """
    Create test application
    """


    app = create_app(
        "testing"
    )



    with app.app_context():


        db.create_all()



        yield app



        db.session.remove()



        db.drop_all()







@pytest.fixture
def client(app):

    """
    Flask Test Client
    """


    return app.test_client()







@pytest.fixture
def database(app):

    """
    Database fixture
    """


    return db