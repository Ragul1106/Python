products = ["Pen", "Notebook", "Eraser", "Scale"]
search = input("Enter product to search: ")
for product in products:
    if product.lower() == search.lower():
        print("Product Found")
        break
else:
    print("Not Found")