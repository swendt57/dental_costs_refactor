import os

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

from data import *
# from data.user import *
from utils.middleware import PrefixMiddleware

app = Flask(__name__)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/dental_costs/herokuapp/')

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
    dentists = dentist.retrieve_all(mongo)
    return render_template('top-ten-affordable.html',
                           title='Top 10 Affordable Dentists',
                           page='.top-ten')


@app.route('/cost-comparisons')
def cost_comparisons():
    return render_template('cost-comparisons.html', title='Dental Cost Comparisons', page='.comparisons')


@app.route('/maps')
def maps():
    return render_template('maps.html', title='Location Maps', page='.maps')


@app.route('/add-dentist')
def add_dentist():
    return render_template('add-dentist.html', title='Add a Dentist', page='.add_dentist')

@app.route('/insert-dentist', methods=['POST'])
def insert_dentist():
    dentist.insert_one(mongo, request)
    return redirect(url_for('add_dentist'))


# using 'environ.get' caused problems, using 'getenv' instead
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '127.0.0.1'),
            port=os.getenv('PORT', '5000'),
            debug=True)
