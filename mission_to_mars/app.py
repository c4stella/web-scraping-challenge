from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_mission')
#conn = 'mongodb://localhost:27017'

#client = pymongo.MongoClient(conn)
#db = client.mars_mission #name of collection goes here


@app.route('/')
def home():

    mars_info = mongo.db.collection.find_one()

    return render_template('index.html', info=mars_info)


@app.route('/scrape')
def scrape():

    mars_data = scrape_mars.scrape_info()

    mongo.db.collection.update_one({}, {'$set': mars_data}, upsert=True)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)