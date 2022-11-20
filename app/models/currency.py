from app.db import db


class CurrencyModel(db.Model):
    __tablename__ = "currency"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, unique=True, nullable=False)

    users = db.relationship("UserModel", back_populates="currency", lazy=True)