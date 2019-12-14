from bson.objectid import ObjectId


def retrieve_all(conn):
    print('in dentist.py')
    dentists = conn.db.dentists.find()
    # print(den.count())
    # for d in den:
    #     print(d['name'])
    #     print(d['address'])
    return dentists


def retrieve_one(conn, dentist_id):
    return conn.db.dental_costs.find_one({'_id': ObjectId(dentist_id)})


def insert_one(conn, request):
    print("INSERT ONE")
    try:
        print(request.form)
        dentists = conn.db.dentists
        dentists.insert_one(request.form.to_dict())
    except:
        return False
    return True
