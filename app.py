import os

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

from data import dentist_dao
# from data.user import *
from utils.middleware import PrefixMiddleware

app = Flask(__name__)
# app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='dental-costs.herokuapp')

# mongodb+srv://root:<password>@myfirstcluster-rltec.mongodb.net/test?retryWrites=true&w=majority

db_user = os.getenv('db_user')
db_pw = os.getenv('db_pw')

app.config['googleApiKey'] = os.getenv('google_api_key')
app.config["MONGO_DBNAME"] = 'task_manager'
app.config[
    "MONGO_URI"] = "mongodb+srv://{0}:{1}@myfirstcluster-rltec.mongodb.net/dental_costs?retryWrites=true&w=majority".format(
    db_user, db_pw)

mongo = PyMongo(app)

print(mongo)


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='Introduction', page='.home')


@app.route('/top-ten-affordable')
def top_ten():
    dentists = dentist_dao.retrieve_all(mongo)  # not yet used...
    return render_template('top-ten-affordable.html',
                           title='Top 10 Affordable Dentists',
                           page='.top-ten')


@app.route('/cost-comparisons')
def cost_comparisons():
    dentists = dentist_dao.retrieve_all(mongo)  # not yet used...
    return render_template('cost-comparisons.html', title='Dental Cost Comparisons', page='.comparisons', body='cost')


@app.route('/maps')
def maps():
    dentists = dentist_dao.retrieve_all(mongo)  # not yet used...
    return render_template('maps.html', title='Location Maps', page='.maps')


@app.route('/get-dentists')
def get_dentists():
    sd_filter = {'area': 'sd'}
    tj_filter = {'area': 'tj'}
    sd_dentists = dentist_dao.retrieve_all_with_filter(mongo, sd_filter)
    tj_dentists = dentist_dao.retrieve_all_with_filter(mongo, tj_filter)
    # dentists = dentist_dao.retrieve_all(mongo)
    return render_template('dentists.html', title='Dental Offices', page='.admin',
                           sd_dentists=sd_dentists, tj_dentists=tj_dentists)


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


@app.route('/user-info')
def user_info():
    return render_template('user-info.html', title='Helpful Hints', page='.admin')


# using 'environ.get' caused problems, using 'getenv' instead
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '127.0.0.1'),
            port=os.getenv('PORT', '5000'),
            debug=True)
