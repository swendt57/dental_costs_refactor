from bson.objectid import ObjectId


# need to validate that username is unique!!

def assemble_user_dict(request):
    return {
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'username': request.form.get('username'),
        'role': 'user'
    }


def retrieve_all(conn):
    users = conn.db.users.find()
    return users


def retrieve_all_with_filter(conn, user_filter):
    try:
        users = conn.db.users.find(user_filter)
        return users
    except:
        return False


def retrieve_one(conn, user_id):
    users = conn.db.users
    user = users.find_one({'_id': ObjectId(user_id)})
    return user


def retrieve_sys_user(conn, username):
    users = conn.db.users
    sys_user = users.find_one({'username': username})
    return sys_user


def insert_one(conn, request):
    try:
        users = conn.db.users
        user_dict = assemble_user_dict(request)
        users.insert_one(user_dict)
    except:
        return False
    return True


def update(conn, request, user_id):
    try:
        users = conn.db.users
        user_dict = assemble_user_dict(request)
        users.update({'_id': ObjectId(user_id)}, user_dict)
    except:
        return False
    return True
