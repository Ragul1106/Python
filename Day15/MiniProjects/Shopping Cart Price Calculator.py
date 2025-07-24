class ProductExistsError(Exception):
    pass

def shopping_cart():
    cart = {}
    total = 0.0
    
    while True:
        try:
            product = input("Enter product name (or 'done' to finish): ")
            if product.lower() == 'done':
                break
                
            if product in cart:
                raise ProductExistsError("Product already in cart")
                
            price = float(input("Enter price: "))
            if price <= 0:
                raise ValueError("Price must be positive")
                
            cart[product] = price
            total += price
            
        except ValueError as e:
            print(f"Error: {e}")
        except ProductExistsError as e:
            print(f"Error: {e}")
        finally:
            print(f"Current total: ${total:.2f}")
    
    print(f"Final total: ${total:.2f}")

shopping_cart()