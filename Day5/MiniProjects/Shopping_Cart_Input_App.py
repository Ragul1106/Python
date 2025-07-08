cart = []
print("Add products to cart (type 'done' to finish):")

while True:
    product = input("Product name: ").strip()
    if product.lower() == 'done':
        break
    if not product:
        continue
    cart.append(product)
else:
    print("\nYour shopping cart:")
    for item in cart:
        print(f"- {item}")