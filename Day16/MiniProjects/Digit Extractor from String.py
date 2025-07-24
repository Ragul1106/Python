class DigitExtractor:
    def __init__(self, text):
        self.text = text
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1
            if char.isdigit():
                return int(char)
        raise StopIteration

print("\nDigit Extractor:")
for digit in DigitExtractor("abc123def456"):
    print(digit)