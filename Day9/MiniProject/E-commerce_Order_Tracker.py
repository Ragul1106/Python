orders = [
    (5001, "Ragul", ("Laptop", "Mouse", "Keyboard")),
    (5002, "Sameera", ("Phone", "Case")),
    (5003, "Heera", ("Monitor", "HDMI Cable"))
]

def show_orders():
    for order in orders:
        order_id, customer, items = order
        print(f"\nOrder #{order_id} - {customer}")
        print("Items:")
        for item in items:
            print(f"- {item}")

show_orders()

print("\nItem counts:")
for _, _, items in orders:
    print(f"{len(items)} items")