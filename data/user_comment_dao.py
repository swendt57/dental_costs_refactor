from flask import session
from bson.objectid import ObjectId
from datetime import datetime
import pymongo

from data import user_dao


def assemble_user_comment_dict(request):
    try:
        return {
            'user_id': session['profile']['id'],
            'dentist': request.form.get('dentist'),
            'comment': request.form.get('comment'),
            'date_posted': datetime.now()
        }
    except:
        return "something is wrong!"

def retrieve_all(conn):
    comments = conn.db.user_comments.find().sort([("date_posted", pymongo.DESCENDING)])

    # STILL WORKING ON JOINS
    # comments = conn.db.user_comments.aggregate([{
    #     '$lookup':
    #         {
    #             'from': 'users',
    #             'localField': "user_id",
    #             'foreignField': "_id",
    #             'as': 'anything'
    #         }
    # }])

    # FOR NOW....
    comment_list = []

    for x in comments:
        x['user'] = user_dao.retrieve_one(conn, x['user_id'])
        x['formatted_date'] = datetime.strftime(x['date_posted'], "%m/%d/%Y")
        # print()
        comment_list.append(x)

    return comment_list


def retrieve_one(conn, comment_id):
    comments = conn.db.user_comments
    comment = comments.find_one({'_id': ObjectId(comment_id)})
    return comment


def insert_one(conn, request):
    try:
        comments = conn.db.user_comments
        user_comment_dict = assemble_user_comment_dict(request)
        comments.insert_one(user_comment_dict)
    except:
        return "something went wrong"
    return True

