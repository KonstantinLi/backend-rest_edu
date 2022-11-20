from app.schemas import RecordSchema
from flask import abort, request
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import IntegrityError
from ..db import db
from ..models import RecordModel

blp = Blueprint("record", __name__, description="operations on record")


@blp.route("/records/<int:record_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, record_id):
        record = RecordModel.query.get_or_404(record_id)
        return record

    def remove(self, record_id):
        record = RecordModel.query.get_or_404(record_id)

        db.session.delete(record)
        db.session.commit()

        return "Record id " + str(record.id) + " was successfully deleted", 204


@blp.route("/records")
class RecordList(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self):
        records = RecordModel.query.all()

        user_id = request.args.get("user")
        category_id = request.args.get("category")

        if user_id and user_id.isdigit():
            records = filter(lambda record: record.user_id == int(user_id), records)

        if category_id and category_id.isdigit():
            records = filter(lambda record: record.category_id == int(category_id), records)

        return records

    @blp.arguments(RecordSchema)
    @blp.response(201, RecordSchema)
    def post(self, record_data):
        record = RecordModel(**record_data)

        try:
            db.session.add(record)
            db.session.commit()
        except IntegrityError:
            return abort(400, "Record with such id already exists")

        return record
