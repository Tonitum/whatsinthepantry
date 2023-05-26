#!/usr/bin/python3
""" Methods and helpers for working with recipes """
from uuid import uuid4
from backend.database import DBHelper


class Recipes():
    def __init__(self, db_path: str) -> None:
        self.db = DBHelper(db_path)

    def get_uuid(self) -> str:
        return uuid4().hex

    def db_to_recipe(self, db_recipe: list) -> dict:
        dict_recipe = {}
        dict_recipe["id"] = db_recipe[0]
        dict_recipe["name"] = db_recipe[1]
        dict_recipe["ingredients"] = db_recipe[2]
        dict_recipe["meal"] = db_recipe[3]
        dict_recipe["cusine"] = db_recipe[4]
        return dict_recipe

    def get_recipe(self, recipe_id) -> dict:
        db_recipe = self.db.execute_db(f"SELECT * FROM recipes WHERE id=?",
                           (recipe_id,))
        if not len(db_recipe) > 0:
            return {}
        return self.db_to_recipe(db_recipe[0])

    def verify_recipe_json(self, recipe_json) -> bool:
        """check and verify that the json blob has everything we expect"""
        expected_keys = [
                "name",
                "meal",
                "cuisine",
                "ingredients"]
        for key in expected_keys:
            if key not in recipe_json.keys():
                return False
        return True

    def create_new_recipe(self, recipe_json) -> str:
        """Creates a new recipe in the recipes table and returns the uuid"""
        id = self.get_uuid()
        # TODO: handle this better
        self.db.execute_db(f"INSERT INTO recipes (id, name, ingredients, cuisine, meal) VALUES (?,?,?,?,?)",
                        (id, recipe_json['name'], recipe_json['ingredients'], recipe_json['cuisine'], recipe_json['meal'])
                       )
        return id

    def delete_recipe(self, recipe_id) -> bool:
        """Delete a recipe from the database, if it exists"""
        self.db.execute_db(f"DELETE FROM recipes WHERE id=?",
                           (recipe_id,))
        return True

    def search_recipe(self, search: dict) -> list:
        """Find and return all rows that match a search key/term"""
        recipes = [] 
        res = self.db.execute_db(f"SELECT * FROM recipes WHERE ? LIKE ?",
                            (search["term"], f"%{search['term']}%"))
        if len(res) == 0:
            return [] 

        for recipe in res:
            print(recipe)
            recipe_dict = self.db_to_recipe(recipe)
            print(recipe_dict)
            recipes.append(recipe_dict)
        return recipes




