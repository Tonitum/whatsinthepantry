#!/usr/bin/python3
from json import JSONEncoder, JSONDecoder, JSONDecodeError
import unittest
import requests

class CreateRecipeTest(unittest.TestCase):
    def test_default_create(self):
        """Test the nominal recipe creation case"""
        recipe_dict = {}
        headers_dict = {}
        headers_dict["Content-Type"] = "application/json"
        # recipe_dict["name"] = "Spaghetti"
        recipe_dict["meal"] = "Dinner"
        recipe_dict["ingredients"] = "spaghetti,red sauce,ground beef, garlic"

        recipe_data = JSONEncoder().encode(recipe_dict)
        response = requests.request("POST",url="http://localhost:5000/recipe/create",
                                data=recipe_data,
                                headers=headers_dict)
        print(response.json())

if __name__ == "__main__":
    unittest.main()
