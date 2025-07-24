class SkipPickIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 2  
        return item

print("\nSkip-Pick Iterator:")
for item in SkipPickIterator([1, 2, 3, 4, 5]):
    print(item)