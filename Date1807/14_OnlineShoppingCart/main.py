from cart_utils.cart_ops import add_to_cart, view_cart, products, categories

cart = {}

def main():
    while True:
        print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Products:")
            for pid, info in products.items():
                print(f"{pid[0]} - {info['name']} (${info['price']}) - Category: {info['category']}")
            print(f"\nAvailable Categories: {categories}")

        elif choice == "2":
            pid = input("Enter Product ID to add to cart: ")
            quantity = int(input("Enter Quantity: "))
            item_id = (pid.strip(),)
            if item_id in products:
                add_to_cart(cart, item_id, quantity)
            else:
                print("Invalid Product ID")

        elif choice == "3":
            view_cart(cart)

        elif choice == "4":
            break
        else:
            print("Invalid input. Try again.")
if __name__ == "__main__":
    main()
