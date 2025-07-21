class Item:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    
    def __str__(self):
        return f"{self.name} (ID: {self.id}) - ${self.price} x {self.quantity}"

class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item):
        self.items[item.id] = item
    
    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False
    
    def update_item(self, item_id, new_quantity):
        if item_id in self.items:
            self.items[item_id].update_quantity(new_quantity)
            return True
        return False
    
    def __contains__(self, item_id):
        return item_id in self.items
    
    def __getitem__(self, item_id):
        return self.items.get(item_id, None)
    
    def __str__(self):
        return f"Inventory with {len(self.items)} items"

class Supplier:
    def __init__(self, name, contact, products):
        self._name = name  
        self._contact = contact  
        self.products = products
    
    @property
    def name(self):
        return self._name
    
    @property
    def contact(self):
        return self._contact
    
    def add_product(self, product):
        self.products.append(product)
    
    def __str__(self):
        return f"Supplier: {self._name} (Contact: {self._contact})"