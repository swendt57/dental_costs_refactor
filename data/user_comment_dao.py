from bson.objectid import ObjectId
import datetime

from data import user_dao

# user_id to come from session scope??


def assemble_user_comment_dict(request):
    print("in assemble dict")
    print(datetime.now())
    return {
        'user_id': '5dfd68c7aa4db2145020570c',
        'dentist': request.form.get('dentist'),
        'comment': request.form.get('comment')
        # 'date_posted': datetime.now()
    }


def retrieve_all(conn):
    comments = conn.db.user_comments.find()

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
        x['formatted_date'] = datetime.date.strftime(x['date_posted'], "%m/%d/%Y")
        # print()
        comment_list.append(x)

    # print(comment_list)
    return comment_list


def retrieve_one(conn, comment_id):
    comments = conn.db.user_comments
    comment = comments.find_one({'_id': ObjectId(comment_id)})
    return comment


def insert_one(conn, request):
    try:
        print("inserting")
        comments = conn.db.user_comments
        print("got collection")
        user_comment_dict = assemble_user_comment_dict(request)
        print(user_comment_dict)
        print("assembled dict")
        # comments.insert_one(request.form.to_dict())
        comments.insert_one(user_comment_dict)
        print("success?")
    except:
        return "something went wrong"
    return True

