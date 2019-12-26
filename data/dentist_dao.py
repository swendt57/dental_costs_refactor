from bson.objectid import ObjectId
import pymongo


def assemble_dentist_dict(request):
    return {
        'name': request.form.get('name'),
        'abbreviation': request.form.get('abbreviation'),
        'address': request.form.get('address'),
        'address2': request.form.get('address2'),
        'city': request.form.get('city'),
        'state': request.form.get('state'),
        'postal_code': request.form.get('postal_code'),
        'area': request.form.get('area'),
        'phone': request.form.get('phone'),
        'website': request.form.get('website'),
        'latitude': float(request.form.get('latitude')),
        'longitude': float(request.form.get('longitude')),
        'cleaning': int(request.form.get('cleaning')),
        'filling': int(request.form.get('filling')),
        'extraction': int(request.form.get('extraction')),
        'root_canal': int(request.form.get('root_canal')),
        'crown': int(request.form.get('crown')),
        'mock_data': bool(request.form.get('mock_data')),
        'is_active': bool(request.form.get('is_active'))
    }


def retrieve_all(conn):
    dentists = conn.db.dentists.find({'is_active': True}).sort([("name", pymongo.ASCENDING)])
    return dentists


def retrieve_all_with_filter(conn, dentist_filter):
    dentists = conn.db.dentists.find(dentist_filter)
    return dentists


def retrieve_one(conn, dentist_id):
    dentists = conn.db.dentists
    dentist = dentists.find_one({'_id': ObjectId(dentist_id)})
    return dentist


def insert_one(conn, request):
    try:
        dentists = conn.db.dentists
        # dentists.insert_one(request.form.to_dict())
        dentist_dict = assemble_dentist_dict(request)
        dentists.insert_one(dentist_dict)
    except:
        return False
    return True


def update(conn, request, dentist_id):
    try:
        dentists = conn.db.dentists
        dentist_dict = assemble_dentist_dict(request)
        dentists.update({'_id': ObjectId(dentist_id)}, dentist_dict)
    except:
        return False
    return True
