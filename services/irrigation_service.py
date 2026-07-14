from database import db
from models.irrigation_history import IrrigationHistory


class IrrigationService:

    @staticmethod
    def calculate(soil_moisture, temperature, humidity):
        """
        Smart Irrigation Calculation
        """

        # Water requirement calculation
        water_required = (
            (100 - soil_moisture) * 0.4 +
            temperature * 0.3 -
            humidity * 0.2
        )

        if water_required < 0:
            water_required = 0

        water_required = round(water_required, 2)

        # Pump Status
        status = "ON" if water_required >= 20 else "OFF"

        # AI Recommendation
        if water_required >= 30:
            recommendation = (
                "High water requirement detected. "
                "Start irrigation immediately."
            )

        elif water_required >= 20:
            recommendation = (
                "Moderate irrigation required. "
                "Best time is early morning or evening."
            )

        elif water_required >= 10:
            recommendation = (
                "Light irrigation recommended."
            )

        else:
            recommendation = (
                "No irrigation required at this time."
            )

        return {

            "soil_moisture": soil_moisture,

            "temperature": temperature,

            "humidity": humidity,

            "water_required": water_required,

            "status": status,

            "recommendation": recommendation

        }

    @staticmethod
    def save(result):
        """
        Save irrigation history.
        """

        try:

            record = IrrigationHistory(

                soil_moisture=result["soil_moisture"],

                temperature=result["temperature"],

                humidity=result["humidity"],

                water_required=result["water_required"],

                status=result["status"],

                recommendation=result["recommendation"]

            )

            db.session.add(record)

            db.session.commit()

            print("Irrigation history saved successfully.")

        except Exception as e:

            db.session.rollback()

            print(f"Database Error: {e}")

                # --------------------------------------------
    # Get Last 20 Irrigation History Records
    # --------------------------------------------

    @staticmethod
    def get_history():

        try:

            records = (
                IrrigationHistory.query
                .order_by(
                    IrrigationHistory.id.desc()
                )
                .limit(20)
                .all()
            )


            history = []


            for record in records:

                history.append({

                    "id": record.id,

                    "soil_moisture":
                        record.soil_moisture,

                    "temperature":
                        record.temperature,

                    "humidity":
                        record.humidity,

                    "water_required":
                        record.water_required,

                    "status":
                        record.status,

                    "recommendation":
                        record.recommendation,

                    "created_at":
                        record.created_at.strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )

                })


            return history


        except Exception as e:

            print(
                "History Error:",
                e
            )

            return []