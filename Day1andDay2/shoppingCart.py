cart = {}
for i in range(3):
    item = input(f"Enter item {i+1} name: ")
    price = float(input(f"Enter {item} price: "))
    cart[item] = price

total = sum(cart.values())
print(f"\nYour items: {cart}")
print(f"Total amount: ${total:.2f}")