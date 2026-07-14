from datetime import datetime
from database import db


class IrrigationHistory(db.Model):
    __tablename__ = "irrigation_history"

    id = db.Column(db.Integer, primary_key=True)

    crop_name = db.Column(db.String(100))

    soil_moisture = db.Column(db.Float)

    temperature = db.Column(db.Float)

    humidity = db.Column(db.Float)

    recommendation = db.Column(db.String(100))

    water_required = db.Column(db.Float)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )