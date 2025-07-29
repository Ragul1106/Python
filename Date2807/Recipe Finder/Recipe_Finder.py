import json
from functools import wraps
from typing import Dict, List, Set, Generator

class Recipe:
    def __init__(self, name: str, ingredients: List[str], steps: List[str]):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
    
    def __str__(self) -> str:
        return self.format_recipe()
    
    def format_recipe(self) -> str:
        """String manipulation to format recipe display"""
        ingredients_str = "\n".join(f"- {ing}" for ing in self.ingredients)
        steps_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(self.steps))
        
        return (
            f"Recipe: {self.name}\n\n"
            f"Ingredients:\n{ingredients_str}\n\n"
            f"Steps:\n{steps_str}\n"
        )

class RecipeFinder:
    def __init__(self, filename: str = "recipes.json"):
        self.filename = filename
        self.recipes: Dict[str, Recipe] = {}
        self.load_recipes()
    
    def load_recipes(self) -> None:
        """File handling: Load recipes from JSON"""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for name, recipe_data in data.items():
                    self.recipes[name] = Recipe(
                        name=name,
                        ingredients=recipe_data['ingredients'],
                        steps=recipe_data['steps']
                    )
        except FileNotFoundError:
            print(f"Warning: {self.filename} not found. Starting with empty recipe list.")
        except json.JSONDecodeError:
            print(f"Error: {self.filename} contains invalid JSON. Starting with empty recipe list.")
    
    def save_recipes(self) -> None:
        """Save recipes to JSON file"""
        data = {
            name: {
                'ingredients': recipe.ingredients,
                'steps': recipe.steps
            }
            for name, recipe in self.recipes.items()
        }
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
    
    def get_unique_ingredients(self) -> Set[str]:
        """Set: Get all unique ingredients across recipes"""
        unique_ingredients = set()
        for recipe in self.recipes.values():
            unique_ingredients.update(recipe.ingredients)
        return unique_ingredients
    
    def search_by_ingredient(self, ingredient: str) -> List[Recipe]:
        """Search recipes containing a given ingredient"""
        matching_recipes = []
        for recipe in self.recipes.values():
            if ingredient.lower() in (ing.lower() for ing in recipe.ingredients):
                matching_recipes.append(recipe)
        return matching_recipes
    
    def add_recipe(self, name: str, ingredients: List[str], steps: List[str]) -> None:
        """Add a new recipe to the collection"""
        if name in self.recipes:
            raise ValueError(f"A recipe with name '{name}' already exists.")
        self.recipes[name] = Recipe(name, ingredients, steps)
        self.save_recipes()
    
    def recipe_generator(self) -> Generator[Recipe, None, None]:
        """Generator: Yield recipes one by one"""
        for recipe in self.recipes.values():
            yield recipe
    
    def find_recipes_with_missing_ingredient(self, ingredient: str) -> List[str]:
        """Exception handling: Find recipes missing a specific ingredient"""
        missing_recipes = []
        for name, recipe in self.recipes.items():
            try:
                if ingredient not in recipe.ingredients:
                    missing_recipes.append(name)
            except Exception as e:
                print(f"Error checking ingredients for {name}: {str(e)}")
        return missing_recipes

def log_search(func):
    """Decorator to track search operations"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print(f"Search performed: {func.__name__} with args {args} and kwargs {kwargs}")
        print(f"Found {len(result)} matching recipes")
        return result
    return wrapper

# Example usage
if __name__ == "__main__":
    finder = RecipeFinder()
    
    # Adding some example recipes if none exist
    if not finder.recipes:
        try:
            finder.add_recipe(
                "Pasta Carbonara",
                ["spaghetti", "eggs", "bacon", "parmesan", "black pepper"],
                ["Boil spaghetti", "Fry bacon", "Mix eggs and cheese", "Combine all ingredients"]
            )
            finder.add_recipe(
                "Vegetable Stir Fry",
                ["bell peppers", "broccoli", "carrots", "soy sauce", "garlic"],
                ["Chop vegetables", "Heat oil in pan", "Stir fry vegetables", "Add soy sauce"]
            )
        except ValueError as e:
            print(e)
    
    # Search with decorator
    @log_search
    def search_and_display(finder: RecipeFinder, ingredient: str):
        """Search and display recipes containing an ingredient"""
        recipes = finder.search_by_ingredient(ingredient)
        for recipe in recipes:
            print(recipe)
        return recipes
    
    # Example searches
    print("Recipes with eggs:")
    search_and_display(finder, "eggs")
    
    print("\nRecipes with garlic:")
    search_and_display(finder, "garlic")
    
    print("\nAll unique ingredients:")
    print(", ".join(finder.get_unique_ingredients()))
    
    print("\nAll recipes (using generator):")
    for recipe in finder.recipe_generator():
        print(recipe.name)