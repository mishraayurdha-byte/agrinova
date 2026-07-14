from datetime import datetime
from database import db


class CropPrediction(db.Model):
    __tablename__ = "crop_predictions"

    id = db.Column(db.Integer, primary_key=True)

    crop_name = db.Column(db.String(100), nullable=False)

    rainfall = db.Column(db.Float)

    temperature = db.Column(db.Float)

    humidity = db.Column(db.Float)

    soil_type = db.Column(db.String(100))

    predicted_yield = db.Column(db.Float)

    recommendation = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )