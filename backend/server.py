#!/usr/bin/python3

""" REST API for interacting with the recipe database """

from flask import Flask
from flask import request
import json


from backend.recipe import verify_recipe_json

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


@app.route("/recipe/create", methods = ["POST"])
def create_recipe():
    """Receive a JSON blob and use it to create a new recipe entry in the database"""
    content_type = request.headers.get("Content-Type")
    print(content_type)
    if content_type != "application/json":
        # TODO: return an error code here
        return json.JSONEncoder().encode({"ERROR": "Must receive JSON"})

    # TODO: verify the provided JSON
    recipe_json = request.json
    if not verify_recipe_json(recipe_json):
        # TODO: return an error code here
        return json.JSONEncoder().encode({"ERROR": "JSON Doesn't contain the expected data"})
    # TODO: use the provided JSON to create a recipe database entry
    response_json = json.JSONEncoder().encode({"recipe_id": "1234"})

    return response_json


@app.route("/recipe/delete")
def delete_recipe():
    return "Recipe!"


@app.route("/recipe/update")
def update_recipe():
    return "Recipe!"

if __name__ == "__main__":
    app.run(port=5000)
