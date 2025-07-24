class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.text[self.index]

print("\nReverse String:")
for char in ReverseString("hello"):
    print(char)