products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger']
search = input("Enter product to search: ")

if search in products:
    print("Available in stock!")
else:
    print("Out of stock")