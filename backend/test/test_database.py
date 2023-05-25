#!/usr/bin/python3

import os
import unittest
import sqlite3

from backend.recipe import Recipes 


class CreateRecipeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.mkdir("temp")

    def setUp(self) -> None:
        self.recipes = Recipes("temp/test.db")

    def _get_recipe(self) -> dict:
        recipe_dict = {}
        recipe_dict["name"] = "Spaghetti"
        recipe_dict["meal"] = "Dinner"
        recipe_dict["ingredients"] = "spaghetti,red sauce,ground beef, garlic"
        recipe_dict["cuisine"] = "Italian"
        return recipe_dict

    def test_create_new_recipe(self):
        """Test the nominal recipe creation case"""
        recipe = self._get_recipe()
        id = self.recipes.create_new_recipe(recipe)

        # verify that the recipe was created correctly
        con = sqlite3.connect(database=f"{self.recipes.db.path}")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM recipes WHERE id IS (?)", (id,))
        rows = res.fetchall()
        self.assertIsNotNone(rows)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], id)

    def tearDown(self) -> None:
        self.recipes.db.close_db()

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove("temp/test.db")
        os.rmdir("temp")


if __name__ == "__main__":
    unittest.main(verbosity=3)
