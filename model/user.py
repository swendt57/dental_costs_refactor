from flask_marshmallow import Schema
from marshmallow import fields, ValidationError


def validate_length(str):
    if len(str) == 0:
        raise ValidationError("is required")


class UserSchema(Schema):
    first_name = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    last_name = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    username = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    role = fields.Str(required=True, default='user')
