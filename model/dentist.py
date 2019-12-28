from flask_marshmallow import Marshmallow, Schema
from marshmallow import fields, ValidationError
from marshmallow.validate import Range


def validate_length(str):
    if len(str) == 0:
        raise ValidationError("is required")


class DentistSchema(Schema):
    name = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    abbreviation = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    address = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    address2 = fields.Str()
    city = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    state = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    postal_code = fields.Str()
    area = fields.Str(required=True, validate=validate_length, error_messages={"required": "is required"})
    phone = fields.Str()
    website = fields.Str()
    latitude = fields.Number(required=True, validate=[Range(min=-90, max=90, error="must be between -90 and 90")])
    longitude = fields.Number(required=True, validate=[Range(min=-180, max=180, error="must be between -180 and 180")])
    cleaning = fields.Int(required=True)
    filling = fields.Int(required=True)
    extraction = fields.Int(required=True)
    root_canal = fields.Int(required=True)
    crown = fields.Int(required=True)
    mock_data = fields.Bool(default=False)
    is_active = fields.Bool(default=False)


