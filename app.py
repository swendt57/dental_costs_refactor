import os

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.json_util import dumps
import time
import json

from data import dentist_dao, user_dao, user_comment_dao
from utils.data_format import *

app = Flask(__name__)

db_user = os.getenv('db_user')
db_pw = os.getenv('db_pw')

app.config['googleApiKey'] = os.getenv('google_api_key')
app.config["MONGO_DBNAME"] = 'dental_costs'
app.config[
    "MONGO_URI"] = "mongodb+srv://{0}:{1}@myfirstcluster-rltec.mongodb.net/dental_costs?retryWrites=true&w=majority".format(
    db_user, db_pw)

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='Introduction', page='.home')


@app.route('/top-ten-affordable')
def top_ten():
    return render_template('top-ten-affordable.html', title='Top 10 Affordable Dentists', page='.top-ten')


@app.route('/cost-comparisons')
def cost_comparisons():
    return render_template('cost-comparisons.html', title='Dental Cost Comparisons', page='.comparisons', body='cost')


@app.route('/maps')
def maps():
    return render_template('maps.html', title='Location Maps', page='.maps')


# **************DENTISTS****************************


@app.route('/get-dentists')
def get_dentists():
    sd_filter = {'area': 'sd'}
    tj_filter = {'area': 'tj'}
    sd_dentists = dentist_dao.retrieve_all_with_filter(mongo, sd_filter)
    tj_dentists = dentist_dao.retrieve_all_with_filter(mongo, tj_filter)

    return render_template('dentists.html', title='Dental Offices', page='.admin',
                           sd_dentists=sd_dentists, tj_dentists=tj_dentists)


@app.route('/export-dentists')
def export_dentists():
    # rename the old json file
    now = time.time()
    os.rename(r'static/data/combined_flat.json', r'static/data/combined_flat_' + str(now) + '.json')

    # get the current active dentist list
    dentists = dentist_dao.retrieve_all_with_filter(mongo, {'is_active': True})
    json_text = dumps(dentists)  # converts cursor to json
    parsed_json = json.loads(json_text)  # parses the json

    # restructure the data
    restructured_json = restructure_dental_json(parsed_json)

    # save the file
    f = open("static/data/combined_flat.json", "w")
    f.write(json.dumps(restructured_json, indent=4))  # write pretty json to the file
    f.close()

    return redirect(url_for('get_dentists'))


# @app.route('/run-tests')
# def run_tests():
#     restructure_dental_json('static/data/combined_flat.json')
#     # copy_elements('static/data/test_out.json')
#     return 'happy!'


@app.route('/add-dentist')
def add_dentist():
    return render_template('add-dentist.html', title='Add a Dentist', page='.admin')


@app.route('/insert-dentist', methods=['POST'])
def insert_dentist():
    dentist_dao.insert_one(mongo, request)
    return redirect(url_for('get_dentists'))


@app.route('/edit-dentist/<dentist_id>')
def edit_dentist(dentist_id):
    dentist = dentist_dao.retrieve_one(mongo, dentist_id)
    print(dentist)
    return render_template('edit-dentist.html', dentist=dentist, title='Edit a Dentist', page='.admin')


@app.route('/update-dentist/<dentist_id>', methods=['POST'])
def update_dentist(dentist_id):
    dentist_dao.update(mongo, request, dentist_id)
    return redirect(url_for('get_dentists'))


# **************USERS****************************

@app.route('/get-users')
def get_users():
    user_filter = {'role': 'user'}
    admin_filter = {'role': 'admin'}
    users = user_dao.retrieve_all_with_filter(mongo, user_filter)
    admins = user_dao.retrieve_all_with_filter(mongo, admin_filter)
    return render_template('users.html', title='System Users', page='.admin', users=users, admins=admins)


@app.route('/add-user')
def add_user():
    return render_template('add-user.html', title='Add a User', page='.admin')


@app.route('/insert-user', methods=['POST'])
def insert_user():
    user_dao.insert_one(mongo, request)
    return redirect(url_for('get_users'))


@app.route('/edit-user/<user_id>')
def edit_user(user_id):
    user = user_dao.retrieve_one(mongo, user_id)
    return render_template('edit-user.html', user=user, title='Edit a User', page='.admin')


@app.route('/update-user/<user_id>', methods=['POST'])
def update_user(user_id):
    user_dao.update(mongo, request, user_id)
    return redirect(url_for('get_users'))


@app.route('/get-user-comments')
def get_comments():
    comments = user_comment_dao.retrieve_all(mongo)
    return render_template('user-comments.html', title='User Comments', page='.comments', comments=comments)


@app.route('/add-comment')
def add_comment():
    all_dentists = dentist_dao.retrieve_all(mongo)
    return render_template('add-comment.html', title='Add a Comment', page='.comments', dentists=all_dentists)


@app.route('/insert-comment', methods=['POST'])
def insert_comment():
    print(request.form)
    user_comment_dao.insert_one(mongo, request)
    return redirect(url_for('get_comments'))


# using 'environ.get' caused problems, using 'getenv' instead
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '127.0.0.1'),
            port=os.getenv('PORT', '5000'),
            debug=True)
