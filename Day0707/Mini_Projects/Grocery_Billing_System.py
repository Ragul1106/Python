items = {'Milk': 50, 'Bread': 30, 'Eggs': 60, 'Rice': 80, 'Oil': 120}
cart = []

print("Available Items:")
for item, price in items.items():
    print(f"{item}: ₹{price}")

while True:
    item = input("Enter item (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    if item in items:
        cart.append(items[item])

total = sum(cart)
if total > 1000:
    total *= 0.9
    print("10% discount applied!")

print(f"\nTotal Bill: ₹{total:.2f}")