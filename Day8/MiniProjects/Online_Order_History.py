orders = ['Order1', 'Order2', 'Order3', 'Order4', 'Order5']

def add_order():
    order = input("Order ID: ")
    orders.append(order)
    print(f"Added {order}")

def show_recent_orders():
    print("\nLast 5 Orders:")
    for order in orders[-5:]:
        print(f"- {order}")
    print(f"\nTotal orders: {len(orders)}")

add_order()
show_recent_orders()