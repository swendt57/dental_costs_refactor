from marshmallow import Schema, fields


class DentistSchema(Schema):
    name = fields.Str(required=True)
    abbr = fields.Str(required=True)
    address = fields.Str(required=True)
    address2 = fields.Str()
    city = fields.Str()
    state = fields.Str()
    postal_code = fields.Str()
    area = fields.Str()
    phone = fields.Str()
    website = fields.Str()
    latitude = fields.Str()
    longitude = fields.Str()
    cleaning = fields.Str()
    filling = fields.Str()
    extraction = fields.Str()
    root_canal = fields.Str()
    crown = fields.Str()
