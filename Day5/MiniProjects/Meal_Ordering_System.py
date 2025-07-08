order = []
print("Enter food items (type 'done' to finish):")

while True:
    item = input("Add item: ").strip()
    if item.lower() == 'done':
        break
    if not item:
        continue
    order.append(item)
else:
    print(f"\nOrder complete! Total items: {len(order)}")
    print("Your order:", ", ".join(order))