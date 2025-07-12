menu = [['Pizza', 12.99], ['Pasta', 9.99]]

def add_dish():
    dish = input("Dish name: ")
    price = float(input("Price: "))
    menu.append([dish, price])

def remove_dish():
    dish = input("Dish to remove: ")
    for item in menu[:]:
        if item[0] == dish:
            menu.remove(item)
            print(f"Removed {dish}")
            return
    print("Dish not found")

def show_menu():
    print("\nMenu:")
    for item in menu:
        print(f"{item[0]}: ${item[1]:.2f}")

add_dish()
remove_dish()
show_menu()