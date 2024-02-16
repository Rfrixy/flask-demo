import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/flights", methods=['POST'])
def flights():
    f = open("./flights.json")
    data = json.load(f)
    return data

@app.route("/flights")
def flights():
    f = open("./flights.json")
    data = json.load(f)
    return data