class CartIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration("Cart is empty")
        item = self.items[self.index]
        self.index += 1
        return item

print("\nCart Items:")
cart = CartIterator(["Apple", "Banana", "Orange"])
print(next(cart))
print(next(cart))