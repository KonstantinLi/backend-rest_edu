from flask_jwt_extended import jwt_required

from app.db import db
from app.models.currency import CurrencyModel
from app.schemas import CurrencySchema
from flask import abort
from flask.views import MethodView

from flask_smorest import Blueprint
from sqlalchemy.exc import IntegrityError

blp = Blueprint("currency", __name__, description="operations on currency")


@blp.route("/currency/<int:id>")
class Currency(MethodView):
    @blp.response(200, CurrencySchema)
    def get(self, id):
        currency = CurrencyModel.query.get_or_404(id)
        return currency


@blp.route("/currency")
class CurrencyList(MethodView):

    @blp.response(200, CurrencySchema(many=True))
    def get(self):
        currency_list = CurrencyModel.query.all()
        return currency_list

    @jwt_required()
    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    def post(self, currency_data):
        currency = CurrencySchema()
        currency.type = currency_data["type"]

        try:
            db.session.add(currency)
            db.session.commit()
        except IntegrityError:
            return abort(400, "Currency with such type already exists")

        return currency
