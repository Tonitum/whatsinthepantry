#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)


@app.route("/")
def root():
    return "Hello world"


@app.route("/recipes")
def get_recipes():
    return "Recipe List"


@app.route("/search/<term>")
def search(term):
    return f"Search by {term}"
