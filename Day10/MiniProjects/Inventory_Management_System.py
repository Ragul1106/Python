inventory = {}

def add_item(name, stock, min_req, supplier):
    inventory[name] = {"stock": stock, "min_required": min_req, "supplier": supplier}

def check_stock():
    return {item: data for item, data in inventory.items() 
            if data["stock"] < data["min_required"]}

add_item("Laptop", 5, 10, "Dell")
print("Low stock:", check_stock())