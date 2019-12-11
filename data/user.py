from bson.objectid import ObjectId


def retrieve_all(conn):
    return conn.db.users.find()
