#!/usr/bin/python3

""" Methods and helpers for working with recipes """


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

