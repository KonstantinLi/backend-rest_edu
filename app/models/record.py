from sqlalchemy import func

from app.db import db


class RecordModel(db.Model):
    __tablename__ = "records"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=False,
        nullable=False
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        unique=False,
        nullable=False
    )

    date = db.Column(db.String, nullable=False)
    pay = db.Column(db.Integer, nullable=False)

    user = db.relationship("UserModel", back_populates="record")
    category = db.relationship("CategoryModel", back_populates="record")
