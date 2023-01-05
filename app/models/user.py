from app.db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    currency_id = db.Column(db.Integer, db.ForeignKey("currency.id"), nullable=False, default=1)

    currency = db.relationship("CurrencyModel", back_populates="users")
    record = db.relationship("RecordModel", back_populates="user")