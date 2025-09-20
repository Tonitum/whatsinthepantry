from pydantic import BaseModel
from backend.src.ingredient import Ingredient


class Recipe(BaseModel):
    recipe_id: int | None = None
    category: str = ""
    ingredients: list[Ingredient] = []
    meal: str = ""
    name: str = ""
