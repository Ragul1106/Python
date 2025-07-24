class WordSplitter:
    def __init__(self, sentence):
        self.words = sentence.split()
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word

print("\nWord Splitter:")
for word in WordSplitter("This is a test sentence"):
    print(word)