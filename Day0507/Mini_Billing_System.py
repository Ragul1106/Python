menu = {'Burger': 120, 'Pizza': 250, 'Pasta': 180, 'Salad': 90}
cart = []

print("Available Items:")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

for _ in range(3):
    item = input("Enter item to add to cart: ")
    if item in menu:
        cart.append(menu[item])

total = sum(cart)
if total > 1000:
    total *= 0.9
    print("10% discount applied!")

print(f"\nTotal Bill: ₹{total:.2f}")