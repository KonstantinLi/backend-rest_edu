from flask import abort, jsonify, request, Response
from flask.views import MethodView
from flask_smorest import Blueprint

from app import data
from app.random_data.user import User as UserModel
from app.schemas import UserSchema

blp = Blueprint("user", __name__, description="operations on user")


def find_user(user_id):
    user = None
    for user1 in data["users"]:
        if user1["id"] == user_id:
            user = user1
    return user


@blp.route("/users/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = find_user(user_id)

        if not user:
            return abort(404, "User not found")

        return user

    def remove(self, user_id):
        user = find_user(user_id)

        if not user:
            return abort(404, "User not found")

        del data["users"][data["users"].index(user)]
        return "User id " + str(user["id"]) + " was successfully deleted", 204


@blp.route("/users")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return data["users"]

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        name = user_data["name"]
        user = UserModel(name).serialize()

        data["users"].append(user)

        return user

