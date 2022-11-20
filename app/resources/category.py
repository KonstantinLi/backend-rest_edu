from app.db import db
from app.models import CategoryModel
from app.schemas import CategorySchema
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import IntegrityError

blp = Blueprint("category", __name__, description="operations on category")


@blp.route("/categories/<int:category_id>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        return category

    def remove(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)

        db.session.delete(category)
        db.session.commit()

        return "Category id " + str(category.id) + " was successfully deleted", 204


@blp.route("/categories")
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, category_data):
        category = CategoryModel(**category_data)

        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            return abort(400, "Category with such id already exists")

        return category
