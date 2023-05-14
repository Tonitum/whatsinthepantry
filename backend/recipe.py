#!/usr/bin/python3

""" Methods and helpers for working with recipes """

def get_uuid() -> str:
    # TODO: flesh this out
    return "randomid"

def verify_recipe_json(recipe_json) -> bool:
    """check and verify that the json blob has everything we expect"""
    expected_keys = [
            "name",
            "meal",
            "ingredients"]
    for key in expected_keys:
        if key not in recipe_json.keys():
            return False
    return True

def create_new_recipe(recipe_json) -> str:
    """Creates a new recipe in the recipes table and returns the uuid"""
    id = get_uuid()
    # open the database cursor
    # write the recipe
    # close the cursor
    # if wrote successfully, return the uuid
    return id
