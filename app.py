import os

from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.json_util import dumps
import time
import json
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

from data import dentist_dao, user_dao, user_comment_dao
from utils.data_format import *
from model.dentist import DentistSchema
from model.user import UserSchema
from model.comment import CommentSchema

app = Flask(__name__)

# Validation stuff
ma = Marshmallow(app)

# Keys
app.secret_key = os.getenv('secret_key')
app.config['googleApiKey'] = os.getenv('google_api_key')

# Database stuff
db_user = os.getenv('db_user')
db_pw = os.getenv('db_pw')

app.config["MONGO_DBNAME"] = 'dental_costs'
app.config[
    "MONGO_URI"] = "mongodb+srv://{0}:{1}@myfirstcluster-rltec.mongodb.net/dental_costs?retryWrites=true&w=majority".format(
    db_user, db_pw)

mongo = PyMongo(app)

# Login stuff
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Introduction', page='.home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']

        user = mongo.db.users.find({'username': request.form['username']})
        json_text = dumps(user)
        parsed_json = json.loads(json_text)
        print(parsed_json)
        if parsed_json:
            session['profile'] = {"id": parsed_json[0]['_id']['$oid'], 'first_name': parsed_json[0]['first_name'],
                                  'last_name': parsed_json[0]['last_name'], 'role': parsed_json[0]['role']}

            # TODO should send them back from whence they came, if possible
            return redirect(url_for('index'))
        else:
            flash("That username is not in the system")

    return render_template('login-form.html', title='Log in', page='.home')


@app.route('/logout')
def logout():
    # remove the username from the session and empty the profile if it exists
    session.pop('username', None)
    session['profile'] = {}

    return render_template('logout.html', title='Logged out', page='.home')


@app.route('/register')
def register():
    return "happy"


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
    if session['profile'] and session['profile']['role'] == 'admin':
        sd_filter = {'area': 'sd'}
        tj_filter = {'area': 'tj'}
        sd_dentists = dentist_dao.retrieve_all_with_filter(mongo, sd_filter)
        tj_dentists = dentist_dao.retrieve_all_with_filter(mongo, tj_filter)

        return render_template('dentists.html', title='Dental Offices', page='.admin',
                               sd_dentists=sd_dentists, tj_dentists=tj_dentists)

    flash("You do not have proper permissions")
    return redirect(url_for('index'))


@app.route('/export-dentists')
def export_dentists():
    if session['profile'] and session['profile']['role'] == 'admin':
        # rename the old json file
        now = time.time()
        os.rename(r'static/data/combined_flat.json', r'static/data/combined_flat_' + str(now) + '.json')

        # get the current active dentist list
        dentists = dentist_dao.retrieve_all_with_filter(mongo, {'is_active': True})
        json_text = dumps(dentists)  # converts cursor to json
        parsed_json = json.loads(json_text)  # parses the json

        # restructure the data
        restructured_json = restructure_data(parsed_json)

        # save the file
        f = open("static/data/combined_flat.json", "w")
        f.write(json.dumps(restructured_json, indent=4))  # write pretty json to the file
        f.close()

        return redirect(url_for('get_dentists'))

    flash("You do not have proper permissions")
    return redirect(url_for('index'))


@app.route('/add-dentist')
def add_dentist():
    if session['profile'] and session['profile']['role'] == 'admin':
        return render_template('add-dentist.html', title='Add a Dentist', page='.admin')

    flash("You do not have proper permissions")
    return redirect(url_for('index'))


@app.route('/insert-dentist', methods=['POST'])
def insert_dentist():
    if session['profile'] and session['profile']['role'] == 'admin':

        try:
            # Validate input
            DentistSchema().load(request.form)

            dentist_dao.insert_one(mongo, request)
            return redirect(url_for('get_dentists'))

        except ValidationError as error:
            if request.method == 'POST':
                for message in error.messages:
                    flash(str(message) + " -- " + error.messages[message][0])
                return render_template('add-dentist.html', dentist=request.form, title='Add a Dentist', page='.admin')

    flash("You do not have proper permissions")
    return redirect(url_for('index'))


@app.route('/edit-dentist/<dentist_id>')
def edit_dentist(dentist_id):
    if session['profile'] and session['profile']['role'] == 'admin':
        dentist = dentist_dao.retrieve_one(mongo, dentist_id)
        print(dentist)
        return render_template('edit-dentist.html', dentist=dentist, title='Edit a Dentist', page='.admin')

    flash("You do not have proper permissions")
    return redirect(url_for('index'))


@app.route('/update-dentist/<dentist_id>', methods=['POST'])
def update_dentist(dentist_id):
    if session['profile'] and session['profile']['role'] == 'admin':

        try:
            # Validate input
            DentistSchema().load(request.form)

            dentist_dao.update(mongo, request, dentist_id)
            return redirect(url_for('get_dentists'))

        except ValidationError as error:
            if request.method == 'POST':
                for message in error.messages:
                    flash(str(message) + " -- " + error.messages[message][0])
                return render_template('edit-dentist.html', dentist=request.form, title='Edit a Dentist', page='.admin')

    flash("You do not have proper permissions")
    return redirect(url_for('index'))


# **************USERS****************************


@app.route('/get-users')
def get_users():
    if session['profile'] and session['profile']['role'] == 'admin':
        user_filter = {'role': 'user'}
        admin_filter = {'role': 'admin'}
        users = user_dao.retrieve_all_with_filter(mongo, user_filter)
        admins = user_dao.retrieve_all_with_filter(mongo, admin_filter)
        return render_template('users.html', title='System Users', page='.admin', users=users, admins=admins)

    flash("You do not have proper permissions")
    return redirect(url_for('index'))


@app.route('/add-user')
def add_user():
    return render_template('add-user.html', title='Add a User', page='.admin')


@app.route('/insert-user', methods=['POST'])
def insert_user():
    try:
        # Validate input
        UserSchema().load(request.form)

        # Check if username is free
        user = user_dao.retrieve_all_with_filter(mongo, {'username': request.form.get('username')})
        # if it is, insert the new user
        if user.count() == 0:
            user_dao.insert_one(mongo, request)
            return render_template('registered.html', title='Registered', page='.home')

        flash("That username is already taken. Please select another.")
        return render_template('add-user.html', user=request.form, title='Add a User', page='.admin')

    except ValidationError as error:
        if request.method == 'POST':
            for message in error.messages:
                # print(message)
                flash(str(message) + " -- " + error.messages[message][0])
            return render_template('add-user.html', user=request.form, title='Add a User', page='.admin')


@app.route('/edit-user/<user_id>')
def edit_user(user_id):
    if session['profile'] and session['profile']['role'] == 'admin':
        user = user_dao.retrieve_one(mongo, user_id)
        return render_template('edit-user.html', user=user, title='Edit a User', page='.admin')

    flash("You do not have proper permissions")
    return redirect(url_for('index'))


@app.route('/update-user/<user_id>', methods=['POST'])
def update_user(user_id):
    try:
        # Validate input
        UserSchema().load(request.form)

        if session['profile'] and session['profile']['role'] == 'admin':
            user_dao.update(mongo, request, user_id)
            return redirect(url_for('get_users'))

        flash("You do not have proper permissions")
        return redirect(url_for('index'))

    except ValidationError as error:
        if request.method == 'POST':
            for message in error.messages:
                # print(message)
                flash(str(message) + " -- " + error.messages[message][0])
            return render_template('add-user.html', user=request.form, title='Add a User', page='.admin')


# **************COMMENTS****************************


@app.route('/get-user-comments')
def get_comments():
    comments = user_comment_dao.retrieve_all(mongo)
    return render_template('user-comments.html', title='User Comments', page='.comments', comments=comments)


@app.route('/add-comment')
def add_comment():
    if session['profile'] and session['profile']['role']:
        all_dentists = dentist_dao.retrieve_all(mongo)
        return render_template('add-comment.html', title='Add a Comment', page='.comments', dentists=all_dentists)

    flash("You must register and/or log in to leave a comment")
    return redirect(url_for('get_comments'))


@app.route('/insert-comment', methods=['POST'])
def insert_comment():
    try:
        # Validate input
        CommentSchema().load(request.form)

        if session['profile'] and session['profile']['role']:
            user_comment_dao.insert_one(mongo, request)
            return redirect(url_for('get_comments'))

        flash("You must log in to leave a comment")
        return redirect(url_for('get_comments'))
    except ValidationError as error:
        all_dentists = dentist_dao.retrieve_all(mongo)
        if request.method == 'POST':
            for message in error.messages:
                flash(str(message) + " -- " + error.messages[message][0])
            return render_template('add-comment.html', user_comment=request.form, dentists=all_dentists,
                                   title='Add a Comment', page='.comments')


# using 'environ.get' caused problems, using 'getenv' instead
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '127.0.0.1'),
            port=os.getenv('PORT', '5000'),
            debug=False)
