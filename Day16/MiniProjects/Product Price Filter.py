class PriceFilter:
    def __init__(self, products, min_price):
        self.products = products
        self.min_price = min_price
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self.index < len(self.products):
            name, price = list(self.products.items())[self.index]
            self.index += 1
            if price > self.min_price:
                return (name, price)
        raise StopIteration

print("\nPrice Filter:")
products = {"Laptop": 1200, "Mouse": 20, "Keyboard": 50}
for name, price in PriceFilter(products, 1000):
    print(f"{name}: ₹{price}")