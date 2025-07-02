grocery_list = []
grocery_list.append(input("Enter first grocery item: "))
grocery_list.append(input("Enter second grocery item: "))
grocery_list.append(input("Enter third grocery item: "))

print("\nYour grocery items:", *grocery_list, sep=", ")
print(f"Type of grocery_list: {type(grocery_list)}")