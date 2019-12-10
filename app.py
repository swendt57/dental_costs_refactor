import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from middleware import PrefixMiddleware

app = Flask(__name__)
app.debug = True
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/dental_costs')

# mongodb+srv://root:<password>@myfirstcluster-rltec.mongodb.net/test?retryWrites=true&w=majority

db_user = os.getenv('db_user')
db_pw = os.getenv('db_pw')

app.config["MONGO_DBNAME"] = 'task_manager'
app.config[
    "MONGO_URI"] = "mongodb+srv://{0}:{1}@myfirstcluster-rltec.mongodb.net/test?retryWrites=true&w=majority".format(
    db_user, db_pw)

mongo = PyMongo(app)

print(mongo)


@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html', title='Introduction', page='.home')


@app.route('/top-ten-affordable.html')
def top_ten():
    return render_template('top-ten-affordable.html', title='Top 10 Affordable Dentists', page='.top-ten')


@app.route('/cost-comparisons.html')
def cost_comparisons():
    return render_template('cost-comparisons.html', title='Dental Cost Comparisons', page='.comparisons')


@app.route('/maps.html')
def maps():
    return render_template('maps.html', title='Location Maps', page='.maps')


if __name__ == '__main__':
    app.run()
