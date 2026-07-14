from datetime import datetime
from database import db


class DiseasePrediction(db.Model):
    __tablename__ = "disease_predictions"

    id = db.Column(db.Integer, primary_key=True)

    image_name = db.Column(db.String(255))

    disease_name = db.Column(db.String(100))

    confidence = db.Column(db.Float)

    treatment = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )