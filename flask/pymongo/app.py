from flask import Flask, render_template, jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')
app.collection = PyMongo(app).db.transactions

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def home():
    """Landing page."""
    transactions = list(app.collection.find())
    return render_template('views/gerador.html', transactions=transactions)

@app.route('/add/<id>')
def transactions(id):
    doc = {"transaction": [{"type": "SYSTEM_NAME", "name": "TXX1", "formats": {"input": "INX01", "output": ["OUT1", "OUT2"]}}], "createdAt": datetime.now(), "task": "000001"}
    print doc[0]['name']
    app.collection.insert_one(doc)
    return "added.. %s"% datetime.now()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404