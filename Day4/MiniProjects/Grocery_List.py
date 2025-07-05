grocery_items = input("Enter grocery items separated by comma: ").split(',')
print("\nGrocery List:")
for index, item in enumerate(grocery_items, start=1):
print(f"{index}. {item.strip()}")