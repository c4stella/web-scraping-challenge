from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)
db = client.db #name of collection goes here


@app.route('/')
def home():
    return ('')

@app.route('/scrape')
def scrape():
    return ('')



if __name__ == "__main__":
    app.run(debug=True)