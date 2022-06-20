from flask import Flask, render_template
import pymongo
import scrape_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)
db = client.mars_mission #name of collection goes here


@app.route('/')
def home():

    #mars_data = mongo.db.collection.find_one()
    return ('')

@app.route('/scrape')
def scrape():
    return ('')


if __name__ == "__main__":
    app.run(debug=True)