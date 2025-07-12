cart = []

def add_items():
    items = input("Enter items to add (comma separated): ").split(',')
    cart.extend([item.strip() for item in items])
    print("Items added!")

def remove_item():
    item = input("Enter item to remove: ")
    if item in cart:
        cart.remove(item)
        print(f"Removed {item}")
    else:
        print("Item not found")

def show_cart():
    print("\nYour Cart:")
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item}")
    print(f"\nTotal items: {len(cart)}")
    print(f"First 3 items: {cart[:3]}")

add_items()
add_items()
show_cart()
remove_item()
show_cart()