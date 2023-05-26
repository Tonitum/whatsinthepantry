#!/usr/bin/python3

""" REST API for interacting with the recipe database """

import json
from flask import Flask, Response
from flask import request

from backend.recipe import Recipes


app = Flask(__name__)

recipes = Recipes("db/recipes.db")

@app.route("/health")
def health():
    return "Healthy!"


@app.route("/recipe/get/<recipe_id>", methods = ["GET"])
def get_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    status_code = 504

    if len(recipe) > 0:
        status_code = 200

    blob = json.dumps(recipe)
    response = Response(blob, status=status_code, mimetype="application/json")
    return response


@app.route("/recipe/create", methods = ["POST"])
def create_recipe():
    """Receive a JSON blob and use it to create a new recipe entry in the
    database"""
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return Response(
                json.dumps({"ERROR": "Must receive JSON"}),
                status=400,
                mimetype="application/json") 

    recipe_json = request.json
    if not recipes.verify_recipe_json(recipe_json):
        return Response(
                json.dumps({"ERROR": "JSON Doesn't contain the expected data"}),
                status=400,
                mimetype="application/json") 

    recipe_id = recipes.create_new_recipe(recipe_json)
    response_json = json.dumps({"id": recipe_id})
    return Response(response_json, status=200, mimetype="application/json")


@app.route("/recipe/delete", methods = ["POST"])
def delete_recipe():
    """Receive a recipe id and, delete it if it exists"""
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return Response(
                json.dumps({"ERROR": "Must receive JSON"}),
                status=400,
                mimetype="application/json") 

    recipe_json = request.json or {"id": ""}

    if recipes.delete_recipe(recipe_json["id"]):
        return Response(status=200)
    return Response(status=504)

@app.route("/recipe/search", methods = ["POST"])
def search_recipe():
    """Receive a search request"""
    content_type = request.headers.get("Content-Type")

    #TODO: DRY this
    if content_type != "application/json":
        return Response(
                json.dumps({"ERROR": "Must receive JSON"}),
                status=400,
                mimetype="application/json") 

    search_json = request.json or {}

    if search_json == {}:
        return Response(
                json.dumps({"ERROR": "Must receive JSON"}),
                status=400,
                mimetype="application/json") 

    response_recipe = recipes.search_recipe(search_json)
    response_json = json.dumps(response_recipe)
    return Response(response_json, status=200, mimetype="application/json")

@app.route("/recipe/update")
def update_recipe():
    return "Recipe!"


if __name__ == "__main__":
    app.run(port=5000)
