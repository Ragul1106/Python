menu = {
    frozenset(['pasta', 'sauce']): 'Pasta Dish',
    frozenset(['chicken', 'rice']): 'Chicken Meal'
}

ingredients = {'pasta', 'sauce'}
print("Matching meal:", menu.get(frozenset(ingredients)))