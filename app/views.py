import os

from flask import jsonify

from app import app
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from .db import db
from .models.currency import CurrencyModel
from .resources.category import blp as CategoryBlueprint
from .resources.currency import blp as CurrencyBlueprint
from .resources.record import blp as RecordBlueprint
from .resources.user import blp as UserBlueprint

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Flask REST API"
app.config["API_VERSION"] = "v1.0.0"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
db.init_app(app)

api = Api(app)

jwt = JWTManager(app)


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({"message": "The token has expired.", "error": "token_expired"}),
        401,
    )


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
            {"message": "Signature verification failed.", "error": "invalid_token"}
        ),
        401,
    )


@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {
                "description": "Request does not contain an access token.",
                "error": "authorization_required",
            }
        ),
        401,
    )


with app.app_context():
    # Опціонально
    db.drop_all()
    db.create_all()

    if len(CurrencyModel.query.all()) == 0:
        currency1 = CurrencyModel(type="Dollar")
        currency2 = CurrencyModel(type="Euro")
        currency3 = CurrencyModel(type="Hryvnia")

        for currency in [currency1, currency2, currency3]:
            db.session.add(currency)
        db.session.commit()

api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(RecordBlueprint)
api.register_blueprint(CurrencyBlueprint)


@app.route("/")
def index():
    return "Welcome to my little project :)"
