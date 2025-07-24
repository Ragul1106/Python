class CapitalWordFinder:
    def __init__(self, text):
        self.words = text.split()
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            if word[0].isupper():
                return word
        raise StopIteration

print("\nCapital Word Finder:")
text = "The Quick Brown Fox jumps Over the Lazy Dog"
for word in CapitalWordFinder(text):
    print(word)