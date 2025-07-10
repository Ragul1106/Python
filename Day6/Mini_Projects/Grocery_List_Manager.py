inventory = [] 

def add_items(**kwargs):
    global inventory
    inventory.extend(kwargs.items())
    return sorted(inventory, key=lambda x: x[0])

def total_items():
    return sum(qty for _, qty in inventory)

print("Added items:", add_items(apple=5, milk=2, bread=1))
print("Total items:", total_items())