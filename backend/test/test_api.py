#!/usr/bin/python3
from json import JSONEncoder
import unittest
import requests

recipe_id = None

class CreateRecipeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.recipe_id = ""
        return super().setUp()

    def test_01_create_nominal(self):
        """Test the nominal recipe creation case"""
        recipe_dict = {}
        headers_dict = {}
        headers_dict["Content-Type"] = "application/json"
        recipe_dict["name"] = "Spaghetti"
        recipe_dict["meal"] = "Dinner"
        recipe_dict["ingredients"] = "spaghetti,red sauce,ground beef, garlic"
        recipe_dict["cuisine"] = "Italian"

        recipe_data = JSONEncoder().encode(recipe_dict)
        response = requests.request("POST",url="http://0.0.0.0:5000/recipe/create",
                                data=recipe_data,
                                headers=headers_dict)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())
        response_data = response.json()
        global recipe_id
        recipe_id = response_data["id"]

    def test_02_get_nominal(self):
        """Test nominal get case"""
        id = recipe_id
        response = requests.request("GET", url=f"http://0.0.0.0:5000/recipe/get/{id}")
        self.assertEqual(response.status_code, 200)

    def test_03_search_nominal(self):
        search = {}
        search["key"] = "ingredients"
        search["term"] = "Spaghetti"

    def test_03_delete_nominal(self):
        """Test that a recipe can be deleted"""
        id = recipe_id
        recipe_dict = {}
        headers_dict = {}
        headers_dict["Content-Type"] = "application/json"
        recipe_dict["id"] = id
        recipe_data = JSONEncoder().encode(recipe_dict)
        response = requests.request("POST",url="http://0.0.0.0:5000/recipe/delete",
                                data=recipe_data,
                                headers=headers_dict)
        self.assertEqual(response.status_code, 200)

        response = requests.request("GET", url=f"http://0.0.0.0:5000/recipe/get/{id}")
        self.assertEqual(response.status_code, 504)

    def test_04_get_none(self):
        """Test case where id is not in db"""
        id = 1234
        response = requests.request("GET", url=f"http://0.0.0.0:5000/recipe/get/{id}")
        self.assertEqual(response.status_code, 504)

    def tearDown(self) -> None:
        return super().tearDown()


if __name__ == "__main__":
    unittest.main(verbosity=2)
