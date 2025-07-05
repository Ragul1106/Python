items = {'Milk': 50, 'Bread': 35, 'Eggs': 60, 'Rice': 80, 'Sugar': 45}
cart = []

print("Available Items:")
for item, price in items.items():
    print(f"{item}: ₹{price}")

for _ in range(int(input("How many items? "))):
    item = input("Enter item name: ")
    if item in items:
        cart.append(items[item])

total = sum(cart)
if len(cart) > 5:
    total -= 50
    print("₹50 discount applied!")

print(f"\nTotal: ₹{total:.2f}")