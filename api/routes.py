"""
API Registration
"""

from api import api_bp

# Import API modules so routes are registered
from api.weather_api import *
from api.disease_api import *
from api.yield_api import *
from api.irrigation_api import *
from api.chat_api import *
from api.analytics_api import *
from api.reports_api import *


def register_api(app):
    """
    Register API Blueprint
    """
    app.register_blueprint(api_bp)