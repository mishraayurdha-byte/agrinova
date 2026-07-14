"""
api/home_api.py

Home Page Routes
"""

from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    """
    Render Home Page
    """
    return render_template("index.html")


@home_bp.route("/home")
def home_page():
    """
    Render Home Page
    """
    return render_template("index.html")