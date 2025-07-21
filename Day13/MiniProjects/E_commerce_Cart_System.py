# Product class
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (₹{self.price})"

# Cart class
class Cart:
    def __init__(self):
        self.items = []  

    def add_product(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)
            print(f"Removed {product.name} from cart.")
        else:
            print("Product not in cart.")

    def __add__(self, other_cart):
        new_cart = Cart()
        new_cart.items = self.items + other_cart.items
        return new_cart

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, product):
        return product in self.items

    def total(self):
        return sum(p.price for p in self.items)

    @staticmethod
    def calculate_tax(amount, tax_rate=0.18):
        return amount * tax_rate

# User class
class User:
    def __init__(self, username):
        self.username = username
        self.cart = Cart()

    def __str__(self):
        return f"User: {self.username}"

# Order class (inherits from Cart)
class Order(Cart):
    def __init__(self, cart, discount=0.0):
        super().__init__()
        self.items = cart.items
        self.discount = discount

    def final_amount(self):
        total = self.total()
        discount_amt = total * self.discount
        tax = self.calculate_tax(total - discount_amt)
        return total - discount_amt + tax

    def summary(self):
        print("\n🧾 Order Summary:")
        for item in self.items:
            print(f" - {item.name}: ₹{item.price}")
        print(f"Subtotal: ₹{self.total()}")
        print(f"Discount: ₹{self.total() * self.discount}")
        print(f"Tax: ₹{self.calculate_tax(self.total() - self.total() * self.discount)}")
        print(f"Total Payable: ₹{self.final_amount()}")



"""
# Create products
p1 = Product(101, "Laptop", 50000)
p2 = Product(102, "Mouse", 1000)
p3 = Product(103, "Keyboard", 2000)

# Create user and add items
user = User("ragul_dev")
user.cart.add_product(p1)
user.cart.add_product(p2)

# Check contains
print(p2 in user.cart)  # True

# Access using index
print(user.cart[1])  # Mouse

# Remove item
user.cart.remove_product(p3)  # Not in cart

# Create an order from cart
order = Order(user.cart, discount=0.1)
order.summary()
"""