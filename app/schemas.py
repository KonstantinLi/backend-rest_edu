from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str(required=True)


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user = fields.Int(required=True)
    category = fields.Int(required=True)
    pay = fields.Int(required=True)
    date = fields.DateTime()
