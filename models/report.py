from datetime import datetime
from database import db


class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)

    report_name = db.Column(db.String(255))

    report_type = db.Column(db.String(50))

    file_path = db.Column(db.String(500))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )