"""
==========================================================
AgriNova AI v2.0

Database Models

Tables:
- Disease Detection History
- Crop Recommendation History
- Fertilizer History
- Weather History
- Yield Prediction History

==========================================================
"""

from datetime import datetime
from database import db


# ==========================================================
# Disease Detection History
# ==========================================================

class DiseaseHistory(db.Model):

    __tablename__ = "disease_history"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    image_name = db.Column(
        db.String(255),
        nullable=False
    )


    crop_name = db.Column(
        db.String(100),
        nullable=True
    )


    disease_name = db.Column(
        db.String(150),
        nullable=False
    )


    confidence = db.Column(
        db.Float,
        nullable=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



# ==========================================================
# Crop Recommendation History
# ==========================================================

class CropRecommendation(db.Model):

    __tablename__ = "crop_recommendation"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    nitrogen = db.Column(
        db.Float
    )


    phosphorus = db.Column(
        db.Float
    )


    potassium = db.Column(
        db.Float
    )


    temperature = db.Column(
        db.Float
    )


    humidity = db.Column(
        db.Float
    )


    rainfall = db.Column(
        db.Float
    )


    recommended_crop = db.Column(
        db.String(100)
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



# ==========================================================
# Fertilizer History
# ==========================================================

class FertilizerHistory(db.Model):

    __tablename__ = "fertilizer_history"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    crop_name = db.Column(
        db.String(100)
    )


    soil_type = db.Column(
        db.String(100)
    )


    fertilizer_name = db.Column(
        db.String(150)
    )


    recommendation = db.Column(
        db.Text
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# ==========================================================
# WeatherHistory History
# ==========================================================

class WeatherHistory(db.Model):

    __tablename__ = "weather_history"

    id = db.Column(db.Integer, primary_key=True)

    city = db.Column(db.String(150))

    temperature = db.Column(db.Float)

    humidity = db.Column(db.Float)

    pressure = db.Column(db.Float)

    wind_speed = db.Column(db.Float)

    condition = db.Column(db.String(100))

    description = db.Column(db.String(255))

    icon = db.Column(db.String(20))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    def to_dict(self):
                return {
                    "city": self.city,
                    "temperature": self.temperature,
                    "humidity": self.humidity,
                    "pressure": self.pressure,
                    "wind_speed": self.wind_speed,
                    "weather": self.condition,
                    "description": self.description,
                    "icon": self.icon,
                    "created_at": self.created_at.strftime("%d-%m-%Y %H:%M")
                }
# ==========================================================
# Yield Prediction History
# ==========================================================

class YieldHistory(db.Model):

    __tablename__ = "yield_history"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    crop_name = db.Column(
        db.String(100)
    )


    area = db.Column(
        db.Float
    )


    production = db.Column(
        db.Float
    )


    predicted_yield = db.Column(
        db.Float
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )