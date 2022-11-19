from flask import abort, request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint

from app import data
from app.schemas import RecordSchema
from app.random_data.record import Record as RecordModel

from datetime import datetime
from .category import find_category
from .user import find_user

blp = Blueprint("record", __name__, description="operations on record")


def find_record(record_id):
    record = None
    for record1 in data["records"]:
        if record1["id"] == record_id:
            record = record1
    return record


@blp.route("/records/<int:record_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, record_id):
        record = find_record(record_id)

        if not record:
            return abort(404, "Record not found")

        return record

    def remove(self, record_id):
        record = find_record(record_id)

        if not record:
            return abort(404, "Record not found")

        del data["records"][data["records"].index(record)]
        return "Record id " + str(record["id"]) + " was successfully deleted", 204


@blp.route("/records")
class RecordList(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self):
        records = data["records"]

        user_id = request.args.get("user")
        category_id = request.args.get("category")

        if user_id and user_id.isdigit():
            records = filter(lambda record: record["user_id"] == int(user_id), records)

        if category_id and category_id.isdigit():
            records = filter(lambda record: record["category_id"] == int(category_id), records)

        return records

    @blp.arguments(RecordSchema)
    @blp.response(201, RecordSchema)
    def post(self, record_data):
        user = record_data["user_id"]
        category = record_data["category_id"]
        pay = record_data["pay"]
        date_time = None

        if not user:
            return abort(404, "User not found")

        if not category:
            return abort(404, "Category not found")

        if "date" in record_data:
            date_time = record_data["date"]
        else:
            date_time = datetime.now()

        record = RecordModel(user, category, date_time, pay).serialize()
        data["records"].append(record)

        return record
