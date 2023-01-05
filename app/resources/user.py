from flask import abort, request
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required
from flask_smorest import Blueprint
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError

from app.db import db
from app.models.user import UserModel
from app.schemas import UserSchema

blp = Blueprint("user", __name__, description="operations on user")


@blp.route("/users/<int:id>")
class User(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        password = request.args.get("password")

        if user and pbkdf2_sha256.verify(password, user.pasword):
            return user
        else:
            abort(400, "Incorrect login or password")


@blp.route("/users")
class UserList(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.response(201, UserSchema)
    def post(self):
        name = request.form.get("name")
        password = request.form.get("password")
        type = request.form.get("type")

        if type:
            if type == "auth":
                user = db.session.query(UserModel).filter(UserModel.username == name).first()

                if user and pbkdf2_sha256.verify(password, user.password):
                    access_token = create_access_token(identity=user.id)
                    user.access_token = access_token
                    return user
                else:
                    abort(400, "Incorrect login or password")

            elif type == "registration":
                user = UserModel(
                    username=name,
                    password=pbkdf2_sha256.hash(password)
                )

                try:
                    db.session.add(user)
                    db.session.commit()
                except IntegrityError:
                    abort(400, "User with such name already exists")

                return user

            else:
                abort(400, "Undefined type " + type)

        else:
            abort(400, "Authorization or registration weren't chosen")


