from app import app
from flask_smorest import Api
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
db.init_app(app)

api = Api(app)

with app.app_context():
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


