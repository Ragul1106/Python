def add_recipe(recipe_db, recipe_id, ingredients, utensils):
    if recipe_id in recipe_db:
        print("Recipe already exists.")
        return

    recipe_db[recipe_id] = {
        "ingredients": [i.strip() for i in ingredients],
        "utensils": set(u.strip() for u in utensils)
    }
    print(f"Recipe '{recipe_id[0]}' added.")

def list_recipes(recipe_db):
    if not recipe_db:
        print("No recipes added.")
        return

    for recipe_id, info in recipe_db.items():
        print(f"\nRecipe: {recipe_id[0]}")
        print(f"Ingredients: {', '.join(info['ingredients'])}")
        print(f"Utensils: {', '.join(info['utensils'])}")
