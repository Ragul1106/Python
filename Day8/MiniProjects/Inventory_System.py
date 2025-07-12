inventory = [['Apple', 10], ['Banana', 15]]

def add_product():
    name = input("Product name: ")
    for item in inventory:
        if item[0] == name:
            print("Product already exists")
            return
    quantity = int(input("Quantity: "))
    inventory.append([name, quantity])

def update_product():
    name = input("Product name: ")
    for item in inventory:
        if item[0] == name:
            item[1] = int(input("New quantity: "))
            return
    print("Product not found")

def show_inventory():
    print("\nCurrent Inventory:")
    for item in inventory:
        print(f"{item[0]}: {item[1]}")

add_product()
update_product()
show_inventory()