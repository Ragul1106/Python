products = {'Laptop': 50000, 'Phone': 25000, 'Tablet': 15000}
cart = []

print("Available Products:")
for product, price in products.items():
    print(f"{product}: ₹{price}")

for _ in range(3):
    item = input("Enter product to add: ")
    if item in products:
        cart.append(products[item])

print(f"\nTotal Bill: ₹{sum(cart):.2f}")