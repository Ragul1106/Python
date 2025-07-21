# MenuItem class
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

# Customer class
class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Customer: {self.name}"

# Order class (composition: has many MenuItems)
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)
        print(f"✅ Added {item.name}")

    def remove_item(self, item_name: str):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"❌ Removed {item.name}")
                return
        print("Item not found in the order.")

    def show_order(self):
        print(f"\n🧾 Order for {self.customer.name}")
        for item in self.items:
            print(f" - {item}")
        print(f"Total before tax: ₹{self.total_before_tax()}")

    def total_before_tax(self):
        return sum(item.price for item in self.items)

# Bill class handles tax and final amount
class Bill:
    tax_rate = 0.05  

    @staticmethod
    def generate(order: Order):
        subtotal = order.total_before_tax()
        tax = subtotal * Bill.tax_rate
        total = subtotal + tax
        print(f"\n--- BILL ---")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax ({Bill.tax_rate * 100}%): ₹{tax:.2f}")
        print(f"Grand Total: ₹{total:.2f}")
        print("Thank you for dining with us!")

    @classmethod
    def update_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate
        print(f"🔄 Tax rate updated to {cls.tax_rate * 100}%")

"""
# Menu
burger = MenuItem("Burger", 120)
pizza = MenuItem("Pizza", 250)
cola = MenuItem("Coke", 40)

# Customer and Order
ragul = Customer("Ragul")
order1 = Order(ragul)

# Add/Remove items
order1.add_item(burger)
order1.add_item(pizza)
order1.add_item(cola)
order1.remove_item("Pizza")

# Show and Bill
order1.show_order()
Bill.generate(order1)

# Optional: Change tax rate
Bill.update_tax_rate(0.10)  # 10%
Bill.generate(order1)
"""