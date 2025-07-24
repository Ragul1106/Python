class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        self.current = self.start
        return self
        
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        num = self.current
        self.current += 1
        return num

print("Custom Range:")
for num in MyRange(3, 7):
    print(num)