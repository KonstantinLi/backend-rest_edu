from datetime import datetime

from flask import abort, jsonify, request, Response
from flask.views import MethodView
from flask_smorest import Blueprint

from app import data
from app.model import Record

blp = Blueprint("user", __name__, description="operations on user")


def find_user(user_id):
    user = None
    for user1 in data["users"]:
        if user1.get_id() == user_id:
            user = user1
    return user


@blp.route("/users/<int:user_id>")
class User(MethodView):
    def get(self, user_id):
        user = find_user(user_id)

        if not user:
            return abort(404, "User not found")

        return user

    def post(self, user_id):
        user = find_user(user_id)

        if not user:
            return abort(404, "User not found")

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
                return abort(404, "Category not found")

            if "date" in request_data:
                date = request_data["date"]
            else:
                date = datetime.now()

            record = Record(user, category, date, request_data["pay"])
            data["records"].append(record)

            return "Record id " + str(record.get_id()) + " was successfully created for user " + user.get_name(), 201

        return Response(status=400)

    def remove(self, user_id):
        user = find_user(user_id)

        if not user:
            return abort(404, "User not found")

        del data["users"][data["users"].index(user)]
        return "User id " + str(user.get_id()) + " was successfully deleted", 204


@blp.route("/users")
class UserList(MethodView):
    def get(self):
        json_users = [user.serialize() for user in data["users"]]
        return jsonify(json_users), 200

    def post(self):
        request_data = request.get_json()

        if request_data and "name" in request_data:
            user = User(request_data["name"])
            data["users"].append(user)

            return "User id " + str(user.get_id()) + " was successfully created", 201

        return Response(status=400)
