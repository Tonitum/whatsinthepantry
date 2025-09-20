from fastapi import FastAPI
from backend.src.recipe import Recipe
from backend.src.recipe_manager import save_recipe, recipe_exists, update_recipe, get_recipe, get_all_recipes
from backend.src.database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    init_db()


# create / update
@app.post("/v1/recipe")
async def upsert_recipe(recipe: Recipe) -> dict[str, int]:
    if recipe.recipe_id and recipe_exists(recipe.recipe_id):
        recipe_id = update_recipe(recipe)
    else:
        recipe_id = save_recipe(recipe)
    return {"id": recipe_id}


# read
@app.get("/v1/recipe")
async def get_single_recipe(recipe_id: int) -> Recipe | None:
    return get_recipe(recipe_id)


# read
@app.get("/v1/recipes")
async def get_recipes() -> list[Recipe]:
    return get_all_recipes()


@app.get("/v1/health")
async def root():
    return {"message": "Healthy!"}
