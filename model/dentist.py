from flask_marshmallow import Marshmallow, Schema, fields
ma = Marshmallow()


class DentistSchema(Schema):
    class Meta:
        fields = ('name', 'address', 'cleaning')

    # abbr = fields.Str()
    # address = fields.Str()
    # address2 = fields.Str()
    # city = fields.Str()
    # state = fields.Str()
    # postal_code = fields.Str()
    # area = fields.Str()
    # phone = fields.Str()
    # website = fields.Str()
    # latitude = fields.Str()
    # longitude = fields.Str()
    # cleaning = fields(int)
    # filling = fields.Str()
    # extraction = fields.Str()
    # root_canal = fields.Str()
    # crown = fields.Str()
    # mock_data = fields.Bool()


