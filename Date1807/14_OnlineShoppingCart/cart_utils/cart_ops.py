products = {
    ('P001',): {"name": "Laptop", "price": 50000, "category": "Electronics"},
    ('P002',): {"name": "Phone", "price": 20000, "category": "Electronics"},
    ('P003',): {"name": "Shoes", "price": 3000, "category": "Footwear"},
}

categories = set(info["category"] for info in products.values())

def add_to_cart(cart, item_id, quantity):
    if item_id in cart:
        cart[item_id]["quantity"] += quantity
    else:
        cart[item_id] = {
            "name": products[item_id]["name"],
            "price": products[item_id]["price"],
            "quantity": quantity
        }
    print(f"{quantity} x {products[item_id]['name']} added to cart.")

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    for pid, item in cart.items():
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{item['name']} - {item['quantity']} x ₹{item['price']} = ₹{subtotal}")
    print(f"Total Amount: ₹{total}")
