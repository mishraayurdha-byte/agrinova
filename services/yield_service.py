from database import db
from database.models import YieldHistory


class YieldService:

    def predict(self, features):
        """
        Temporary yield prediction logic.
        Replace this with a trained ML model later.
        """

        rainfall = features[0]
        temperature = features[1]
        humidity = features[2]
        nitrogen = features[3]
        phosphorus = features[4]
        potassium = features[5]

        prediction = (
            (rainfall * 0.02) +
            (temperature * 0.15) +
            (humidity * 0.03) +
            (nitrogen * 0.05) +
            (phosphorus * 0.04) +
            (potassium * 0.03)
        )

        return round(prediction, 2)

    def save(self, data):

        record = YieldHistory(
            crop=data["crop"],
            rainfall=data["rainfall"],
            temperature=data["temperature"],
            humidity=data["humidity"],
            nitrogen=data["nitrogen"],
            phosphorus=data["phosphorus"],
            potassium=data["potassium"],
            prediction=data["prediction"]
        )

        db.session.add(record)
        db.session.commit()