class EmailParser:
    def __init__(self, lines):
        self.lines = lines
        self.index = 0
        self.pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self.index < len(self.lines):
            line = self.lines[self.index]
            self.index += 1
            if re.match(self.pattern, line.strip()):
                return line.strip()
        raise StopIteration

print("\nEmail Parser:")
emails = EmailParser(["test@example.com", "invalid", "user@domain.org"])
for email in emails:
    print("Valid email:", email)