from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    currency_id = fields.Int(required=False)
    access_token = fields.Str(required=False)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    pay = fields.Int(required=True)
    date = fields.Str()


class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str(required=True)
