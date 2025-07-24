class EvenOddSplitter:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
        
    def evens(self):
        for num in self.numbers:
            if num % 2 == 0:
                yield num
                
    def odds(self):
        for num in self.numbers:
            if num % 2 != 0:
                yield num

print("\nEven-Odd Splitter:")
splitter = EvenOddSplitter([1, 2, 3, 4, 5])
print("Evens:", list(splitter.evens()))
print("Odds:", list(splitter.odds()))