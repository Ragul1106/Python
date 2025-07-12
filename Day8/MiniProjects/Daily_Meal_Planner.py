meals = [
    ["Monday", "Oatmeal"],
    ["Tuesday", "Salad"]
]

def add_meal():
    day = input("Day: ")
    meal = input("Meal: ")
    meals.append([day, meal])

def show_weekend_meals():
    print("\nWeekend Meals:")
    for meal in meals[-2:]:
        print(f"{meal[0]}: {meal[1]}")

add_meal()
show_weekend_meals()