from recipe_book.recipe_ops import add_recipe, list_recipes

recipes = {}

def main():
    while True:
        print("\n1. Add Recipe\n2. View Recipes\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Enter Recipe Title: ")
            ingredients = input("Enter Ingredients (comma-separated): ").split(",")
            utensils = input("Enter Utensils (comma-separated): ").split(",")
            recipe_id = (title.strip(),)
            add_recipe(recipes, recipe_id, ingredients, utensils)
        elif choice == "2":
            list_recipes(recipes)
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()