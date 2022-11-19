from flask import abort, jsonify, request, Response
from flask.views import MethodView
from flask_smorest import Blueprint

from app import data

blp = Blueprint("category", __name__, description="operations on category")


def find_category(category_id):
    category = None
    for category1 in data["categories"]:
        if category1.get_id() == category_id:
            category = category1
    return category


@blp.route("/categories/<int:category_id>")
class Category(MethodView):
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
        return "Category id " + str(category.get_id()) + " was successfully deleted", 204


@blp.route("/categories")
class CategoryList(MethodView):
    def get(self):
        json_categories = [category.serialize() for category in data["categories"]]
        return jsonify(json_categories), 200

    def post(self):
        request_data = request.get_json()

        if request_data and "type" in request_data:
            category = Category(request_data["type"])
            data["categories"].append(category)

            return "Category id " + str(category.get_id()) + " was successfully created", 201

        return Response(status=400)