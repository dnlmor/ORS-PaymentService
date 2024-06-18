from datetime import datetime
from app import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default='pending')
    address = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
