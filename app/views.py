from datetime import datetime

from flask import url_for, redirect, request, jsonify, Response

from app import app, data
from .model import User, Category, Record


@app.route("/")
def index():
    return redirect(url_for("get_users"), code=302)


@app.route("/users", methods=["GET"])
def get_users():
    json_users = [user.serialize() for user in data["users"]]
    return jsonify(json_users), 200


@app.route("/users", methods=["POST"])
def post_user():
    request_data = request.get_json()

    if request_data and "name" in request_data:
        user = User(request_data["name"])
        data["users"].append(user)

        return "User id " + str(user.get_id()) + " was successfully created", 201

    return Response(status=400)


@app.route("/categories", methods=["GET"])
def get_categories():
    json_categories = [category.serialize() for category in data["categories"]]
    return jsonify(json_categories), 200


@app.route("/categories", methods=["POST"])
def post_category():
    request_data = request.get_json()

    if request_data and "type" in request_data:
        category = Category(request_data["type"])
        data["categories"].append(category)

        return "Category id " + str(category.get_id()) + " was successfully created", 201

    return Response(status=400)


@app.route("/users/<id>", methods=["POST"])
def post_record(id):
    user = None
    for user1 in data["users"]:
        if id.isdigit() and user1.get_id() == int(id):
            user = user1

    if not user:
        return "User not found", 404

    request_data = request.get_json()
    date = None
    category = None

    if request_data and "category" in request_data and request_data and "pay" in request_data:
        for category1 in data["categories"]:
            category_id = request_data["category"]
            if category1.get_id() == category_id:
                category = category1
                break

        if not category:
            return "Category not found", 404

        if "date" in request_data:
            date = request_data["date"]
        else:
            date = datetime.now()

        record = Record(user, category, date, request_data["pay"])
        data["records"].append(record)

        return "Record id " + str(record.get_id()) + " was successfully created for user " + user.get_name(), 201

    return Response(status=400)


@app.route("/records", methods=["GET"])
def get_record():
    records = data["records"]

    user_id = request.args.get("user")
    category_id = request.args.get("category")

    if user_id and user_id.isdigit():
        records = filter(lambda record: record.get_user().get_id() == int(user_id), records)

    if category_id and category_id.isdigit():
        records = filter(lambda record: record.get_category().get_id() == int(category_id), records)

    json_records = [record.serialize() for record in records]
    return jsonify(json_records), 200


