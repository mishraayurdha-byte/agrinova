"""
==========================================================
AgriNova AI v2.0

Database Initialization

Handles:
- SQLAlchemy setup
- Database instance

==========================================================
"""

from flask_sqlalchemy import SQLAlchemy


# ==========================================================
# Database Object
# ==========================================================

db = SQLAlchemy()