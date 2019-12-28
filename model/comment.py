from flask_marshmallow import Schema
from marshmallow import fields, ValidationError


def validate_length(str):
    if len(str) == 0:
        raise ValidationError("is required")


class CommentSchema(Schema):
    dentist = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    comment = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    user_id = fields.Str()
    date_posted = fields.Str()
