from backend.src.recipe import Recipe
from backend.src.ingredient import Ingredient
from backend.src.database import get_db


def recipe_exists(recipe_id: int) -> bool:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM recipes WHERE id = ?", (recipe_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists


def save_recipe(recipe: Recipe) -> int:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recipes (name, category, meal) VALUES (?, ?, ?)", (recipe.name, recipe.category, recipe.meal))
    recipe_id = cursor.lastrowid
    for ing in recipe.ingredients:
        cursor.execute("INSERT INTO ingredients (recipe_id, name) VALUES (?, ?)", (recipe_id, ing.name))
    conn.commit()
    conn.close()
    return recipe_id


def update_recipe(recipe: Recipe) -> int:
    if not recipe.recipe_id:
        return save_recipe(recipe)
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE recipes SET name=?, category=?, meal=? WHERE id=?", (recipe.name, recipe.category, recipe.meal, recipe.recipe_id))
    cursor.execute("DELETE FROM ingredients WHERE recipe_id=?", (recipe.recipe_id,))
    for ing in recipe.ingredients:
        cursor.execute("INSERT INTO ingredients (recipe_id, name) VALUES (?, ?)", (recipe.recipe_id, ing.name))
    conn.commit()
    conn.close()
    return recipe.recipe_id


def get_recipe(recipe_id: int) -> Recipe | None:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, meal FROM recipes WHERE id=?", (recipe_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return None
    recipe = Recipe(recipe_id=row[0], name=row[1], category=row[2], meal=row[3])
    cursor.execute("SELECT name FROM ingredients WHERE recipe_id=?", (recipe_id,))
    ings = cursor.fetchall()
    recipe.ingredients = [Ingredient(name=ing[0]) for ing in ings]
    conn.close()
    return recipe


def get_all_recipes() -> list[Recipe]:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, meal FROM recipes")
    rows = cursor.fetchall()
    recipes = []
    for row in rows:
        recipe = Recipe(recipe_id=row[0], name=row[1], category=row[2], meal=row[3])
        cursor.execute("SELECT name FROM ingredients WHERE recipe_id=?", (row[0],))
        ings = cursor.fetchall()
        recipe.ingredients = [Ingredient(name=ing[0]) for ing in ings]
        recipes.append(recipe)
    conn.close()
    return recipes
