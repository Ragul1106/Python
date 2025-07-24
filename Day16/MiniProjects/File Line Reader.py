class FileLineReader:
    def __init__(self, filename):
        self.file = open(filename)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while True:
            line = next(self.file).strip()
            if line:  
                return line

with open('test.txt', 'w') as f:
    f.write("Line 1\n\nLine 3\n")
print("\nFile Line Reader:")
for line in FileLineReader('test.txt'):
    print(line)