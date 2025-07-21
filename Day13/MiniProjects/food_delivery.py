class User:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class Customer(User):
    def __init__(self, name, address, phone, payment_method):
        super().__init__(name, address, phone)
        self.payment_method = payment_method
        self.orders = []
    
    def place_order(self, restaurant, items):
        order = Order(self, restaurant, items)
        self.orders.append(order)
        return order

class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu
    
    def __str__(self):
        return f"{self.name} ({self.cuisine})"

class Order:
    def __init__(self, customer, restaurant, items):
        self.customer = customer
        self.restaurant = restaurant
        self.items = items
        self.status = "Placed"
        self.delivery = None
    
    def assign_delivery(self, delivery_agent):
        self.delivery = delivery_agent
        self.status = "Assigned"
    
    def __str__(self):
        return f"Order from {self.restaurant.name} for {self.customer.name} ({self.status})"

class Delivery:
    def deliver(self, order):
        print(f"Delivering order to {order.customer.name}")
        order.status = "Delivered"
        return True

class StandardDelivery(Delivery):
    def deliver(self, order):
        print(f"Standard delivery in progress to {order.customer.address}")
        order.status = "Delivered"
        return True

class ExpressDelivery(Delivery):
    def deliver(self, order):
        print(f"Express delivery! Rush order to {order.customer.address}")
        order.status = "Delivered"
        return True