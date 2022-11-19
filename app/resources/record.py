from flask import abort, request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint

from app import data

blp = Blueprint("record", __name__, description="operations on record")


def find_record(record_id):
    record = None
    for record1 in data["records"]:
        if record1.get_id() == record_id:
            record = record1
    return record


@blp.route("/records/<int:record_id>")
class Record(MethodView):
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
        return "Record id " + str(record.get_id()) + " was successfully deleted", 204


@blp.route("/records")
class RecordList(MethodView):
    def get(self):
        records = data["records"]

        user_id = request.args.get("user")
        category_id = request.args.get("category")

        if user_id and user_id.isdigit():
            records = filter(lambda record: record.get_user().get_id() == int(user_id), records)

        if category_id and category_id.isdigit():
            records = filter(lambda record: record.get_category().get_id() == int(category_id), records)

        json_records = [record.serialize() for record in records]
        return jsonify(json_records), 200

