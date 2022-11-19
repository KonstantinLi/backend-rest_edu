from flask import abort, jsonify, request, Response
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import IntegrityError

from app import data
from app.db import db
from app.models.user import UserModel
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
        user = UserModel.query.get_or_404(user_id)
        return user

    def remove(self, user_id):
        user = UserModel.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return "User id " + str(user.id) + " was successfully deleted", 204


@blp.route("/users")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, "User with such name already exists")

        return user

