cart = {}

def add_item(item, quantity, price):
    cart[item] = {"quantity": quantity, "price": price}

def update_item(item, quantity=None, price=None):
    if item in cart:
        if quantity: cart[item]["quantity"] = quantity
        if price: cart[item]["price"] = price

def remove_item(item):
    cart.pop(item, None)

def total_bill():
    return sum(d["quantity"] * d["price"] for d in cart.values())

def highest_value_item():
    return max(cart.items(), 
              key=lambda x: x[1]["quantity"] * x[1]["price"])[0]

add_item("Laptop", 1, 50000)
add_item("Mouse", 2, 500)
print("Total:", total_bill())
print("Highest value:", highest_value_item())