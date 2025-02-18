import uuid
from database import db
from datetime import datetime

class Expense(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    description = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Float, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(100), nullable=False)
    paidAt = db.Column(db.Date, nullable=True)
    dueAt = db.Column(db.Date, nullable=False)