from app.db import db


class CategoryModel(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    record = db.relationship("RecordModel", back_populates="category")