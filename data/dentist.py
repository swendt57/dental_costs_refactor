from bson.objectid import ObjectId


def retrieve_all(conn):
    print('in dentist.py')
    den = conn.db.dentists.find()
    # print(den.count())
    # for d in den:
    #     print(d['name'])
    #     print(d['address'])
    return den


def retrieve_one(conn, dentist_id):
    return conn.db.dental_costs.find_one({'_id': ObjectId(dentist_id)})
