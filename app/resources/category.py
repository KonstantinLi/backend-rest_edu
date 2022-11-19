from flask import abort, jsonify, request, Response
from flask.views import MethodView
from flask_smorest import Blueprint

from app import data
from app.random_data.category import Category as CategoryModel
from app.schemas import CategorySchema

blp = Blueprint("category", __name__, description="operations on category")


def find_category(category_id):
    category = None
    for category1 in data["categories"]:
        if category1["id"] == category_id:
            category = category1
    return category


@blp.route("/categories/<int:category_id>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        category = find_category(category_id)

        if not category:
            return abort(404, "Category not found")

        return category

    def remove(self, category_id):
        category = find_category(category_id)

        if not category:
            return abort(404, "Category not found")

        del data["categories"][data["categories"].index(category)]
        return "Category id " + str(category["id"]) + " was successfully deleted", 204


@blp.route("/categories")
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return data["categories"]

    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, category_data):
        type = category_data["type"]
        category = CategoryModel(type).serialize()

        data["categories"].append(category)

        return category
