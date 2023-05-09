#!/usr/bin/python3

""" REST API for interacting with the recipe database """

from flask import Flask
import json

app = Flask(__name__)


@app.route("/health")
def health():
    return "Healthy!"


@app.route("/recipe/get/<recipe_id>", methods = ["GET"])
def get_recipe(recipe_id):
    # check that the recipe id exists
    # if it does not, return an error
    # if it does, pull it from the database
    # return the json blob
    response_data = {}
    response_data['status'] = 200
    response_data['id'] = recipe_id
    blob = json.dumps(response_data)
    return blob 


@app.route("/recipe/create")
def create_recipe():
    return "Recipe!"


@app.route("/recipe/delete")
def delete_recipe():
    return "Recipe!"


@app.route("/recipe/update")
def update_recipe():
    return "Recipe!"

if __name__ == "__main__":
    app.run()
