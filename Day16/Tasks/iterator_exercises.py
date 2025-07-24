# ======================
# 1. Basic Iterator and Iterable Understanding 
# ======================

print("\n=== 1. Basic Iterator Exercises ===\n")

# 1.1 Manual list iteration with iter()/next()
print("\n1.1 Manual list iteration:")
colors = ['red', 'green', 'blue']
color_iter = iter(colors)
print(next(color_iter)) 
print(next(color_iter))  
print(next(color_iter))  

# 1.2 For loop vs while with next() on tuple
print("\n1.2 Tuple iteration comparison:")
dimensions = (1920, 1080)

print("For loop:")
for dim in dimensions:
    print(dim)

print("While with next():")
dim_iter = iter(dimensions)
while True:
    try:
        print(next(dim_iter))
    except StopIteration:
        break

# 1.3 Check iterability with dir()
print("\n1.3 Iterability check:")
def is_iterable(obj):
    return '__iter__' in dir(obj)

print(is_iterable([1, 2, 3]))  
print(is_iterable(3.14))       
print(is_iterable("text"))     

# 1.4 Handle next() on non-iterator
print("\n1.4 Handle non-iterator:")
try:
    next(42)
except TypeError as e:
    print(f"Error: {e}")

# 1.5 First 3 elements of set
print("\n1.5 First 3 set elements:")
unique_nums = {5, 3, 8, 1, 9}
set_iter = iter(unique_nums)
for _ in range(3):
    print(next(set_iter))

# 1.6 String character iteration
print("\n1.6 String iteration:")
word = "Python"
char_iter = iter(word)
print(next(char_iter))  # P
print(next(char_iter))  # y

# 1.7 Dictionary key iteration
print("\n1.7 Dictionary keys:")
person = {'name': 'Alice', 'age': 30}
key_iter = iter(person)
print(next(key_iter))  
print(next(key_iter))  

# 1.8 Range to iterator
print("\n1.8 Range iteration:")
range_iter = iter(range(2, 6))
print(next(range_iter))  # 2
print(next(range_iter))  # 3

# 1.9 Print items with next() function
print("\n1.9 Print with next():")
def print_iterable(items):
    it = iter(items)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

print_iterable(['A', 'B', 'C'])

# 1.10 StopIteration handling
print("\n1.10 StopIteration handling:")
values = [10, 20]
val_iter = iter(values)
try:
    print(next(val_iter))
    print(next(val_iter))
    print(next(val_iter))  
except StopIteration:
    print("End reached")

# ======================
# 2. Custom Iterator Classes 
# ======================

print("\n=== 2. Custom Iterator Classes ===")

# 2.1 Countdown iterator
print("\n2.1 Countdown iterator:")
class Countdown:
    def __init__(self, start):
        self.current = start
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

for num in Countdown(3):
    print(f"T-{num}")

# 2.2 Even numbers iterator
print("\n2.2 Even numbers iterator:")
class EvenNumbers:
    def __init__(self, max):
        self.current = 0
        self.max = max
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        num = self.current
        self.current += 2
        return num

for even in EvenNumbers(8):
    print(even)

# 2.3 String character iterator
print("\n2.3 Character iterator:")
class CharIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        char = self.string[self.index]
        self.index += 1
        return char

for char in CharIterator("hello"):
    print(char.upper())

# 2.4 Fibonacci iterator
print("\n2.4 Fibonacci iterator:")
class FibonacciIterator:
    def __init__(self, limit):
        self.a, self.b = 0, 1
        self.limit = limit
        self.count = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

for fib in FibonacciIterator(7):
    print(fib)

# 2.5 Reverse list iterator
print("\n2.5 Reverse list iterator:")
class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

for item in ReverseListIterator([1, 2, 3]):
    print(item)

# 2.6 Square number iterator
print("\n2.6 Square iterator:")
class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        square = self.current ** 2
        self.current += 1
        return square

for sq in SquareIterator(1, 5):
    print(sq)

# 2.7 Letter position iterator
print("\n2.7 Letter position iterator:")
class LetterPositionIterator:
    def __init__(self, word):
        self.word = word
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
        letter = self.word[self.index]
        position = self.index + 1
        self.index += 1
        return (letter, position)

for letter, pos in LetterPositionIterator("world"):
    print(f"{letter} at position {pos}")

# 2.8 Conditional countdown
print("\n2.8 Conditional countdown:")
class CountdownWithStop:
    def __init__(self, start, stop_at):
        self.current = start
        self.stop_at = stop_at
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current <= self.stop_at:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

for num in CountdownWithStop(10, 7):
    print(num)

# 2.9 Vowel extractor
print("\n2.9 Vowel iterator:")
class VowelIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.vowels = {'a', 'e', 'i', 'o', 'u'}
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self.index < len(self.text):
            char = self.text[self.index].lower()
            self.index += 1
            if char in self.vowels:
                return char
        raise StopIteration

for vowel in VowelIterator("Hello World"):
    print(vowel)

# 2.10 Digit extractor
print("\n2.10 Digit iterator:")
class DigitIterator:
    def __init__(self, mixed_str):
        self.text = mixed_str
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

for digit in DigitIterator("a1b2c3"):
    print(digit)

# ======================
# 3. Advanced iter() Usage 
# ======================

print("\n=== 3. Advanced iter() Techniques ===")

# 3.1 Sentinel-based input
print("\n3.1 Input until 'quit':")
# Uncomment to test:
# for cmd in iter(lambda: input("Command: "), "quit"):
#     print(f"Executing: {cmd}")

# 3.2 File reader with sentinel
print("\n3.2 File reader:")
def file_line_reader(filename):
    with open(filename) as f:
        for line in iter(f.readline, ''):
            yield line.strip()

# 3.3 Random number generator
print("\n3.3 Random numbers > 90:")
import random
random_iter = iter(lambda: random.randint(1, 100), 101)
count = 0
for num in random_iter:
    print(num)
    count += 1
    if num > 90:
        break
print(f"Generated {count} numbers")

# 3.4 Number input until 0
print("\n3.4 Number input:")
# Uncomment to test:
# print("Enter numbers (0 to stop):")
# for num in iter(lambda: int(input("Number: ")), 0):
#     print(f"Added {num}")

# 3.5 Alphabet filter
print("\n3.5 Alphabet filter:")
def alpha_filter(text):
    return (c for c in text if c.isalpha())

for char in alpha_filter("a1b@2c#3"):
    print(char)

# 3.6 Infinite number stream
print("\n3.6 Infinite numbers:")
import itertools
numbers = iter(lambda: random.randint(1,10), -1)
for num in itertools.islice(numbers, 5):  
    print(num)

# 3.7 Calculator input
print("\n3.7 Calculator input:")
# Uncomment to test:
# calc_iter = iter(input, "done")
# for expr in calc_iter:
#     print(f"Result: {eval(expr)}")

# 3.8 Lazy square roots
print("\n3.8 Lazy square roots:")
import math
nums = [4, 9, 16, 25]
sqrt_iter = iter((math.sqrt(n) for n in nums))
print(next(sqrt_iter))
print(next(sqrt_iter))

# 3.9 Generic iterable processor
print("\n3.9 Generic processor:")
def process_iterable(iterable):
    it = iter(iterable)
    index = 0
    while True:
        try:
            item = next(it)
            print(f"Item {index}: {item}")
            index += 1
        except StopIteration:
            break

process_iterable(['X', 'Y', 'Z'])

# 3.10 Sentinel with counter
print("\n3.10 Sentinel counter:")
def random_high():
    return random.randint(80, 100)

high_iter = iter(random_high, 95)
count = 0
for num in high_iter:
    print(num)
    count += 1
print(f"Loop ran {count} times")

# ======================
# 4. File Iterators
# ======================

print("\n=== 4. File Iterator Exercises ===")

# Create test file
with open('test_file.txt', 'w') as f:
    f.write("First line\n\nThird line\nFourth line\n\nLast line")

# 4.1 Manual file iteration
print("\n4.1 Manual file reading:")
with open('test_file.txt') as f:
    file_iter = iter(f)
    try:
        print(next(file_iter).strip())
        print(next(file_iter).strip())  
        print(next(file_iter).strip())
    except StopIteration:
        print("End of file")

# 4.2 Handle file end
print("\n4.2 File end handling:")
with open('test_file.txt') as f:
    while True:
        try:
            print(next(f).strip())
        except StopIteration:
            print("EOF reached")
            break

# 4.3 Non-empty lines iterator
print("\n4.3 Non-empty lines:")
class NonEmptyLines:
    def __init__(self, filename):
        self.file = open(filename)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while True:
            line = next(self.file).strip()
            if line:  
                return line

    def __del__(self):
        self.file.close()

try:
    for line in NonEmptyLines('test_file.txt'):
        print(line)
except StopIteration:
    print("Done")

# 4.4 First word extractor
print("\n4.4 First words:")
class FirstWordIterator:
    def __init__(self, filename):
        self.file = open(filename)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        line = next(self.file).strip()
        return line.split()[0] if line else self.__next__()

    def __del__(self):
        self.file.close()

try:
    for word in FirstWordIterator('test_file.txt'):
        print(word)
except StopIteration:
    print("Complete")

# 4.5 Lines with >3 words
print("\n4.5 Filtered lines:")
def long_lines(filename):
    with open(filename) as f:
        for line in f:
            words = line.strip().split()
            if len(words) > 2:  
                yield line.strip()

for line in long_lines('test_file.txt'):
    print(line)

# ======================
# 5. Real-World Iterators 
# ======================

print("\n=== 5. Practical Iterator Examples ===")

# 5.1 Pagination system
print("\n5.1 Pagination:")
class Paginator:
    def __init__(self, items, per_page):
        self.items = items
        self.per_page = per_page
        self.page = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        start = self.page * self.per_page
        if start >= len(self.items):
            raise StopIteration
        self.page += 1
        return self.items[start:start+self.per_page]

posts = [f"Post {i}" for i in range(1, 11)]
for page in Paginator(posts, 3):
    print(f"Page contains: {page}")

# 5.2 Transaction batches
print("\n5.2 Transaction batches:")
class TransactionBatcher:
    def __init__(self, txs, batch_size):
        self.txs = txs
        self.batch_size = batch_size
        self.pos = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.pos >= len(self.txs):
            raise StopIteration
        batch = self.txs[self.pos:self.pos+self.batch_size]
        self.pos += self.batch_size
        return batch

transactions = [f"TX{i:03}" for i in range(1, 16)]
for batch in TransactionBatcher(transactions, 4):
    print(f"Processing: {batch}")

# 5.3 Sensor data monitor
print("\n5.3 Sensor monitor:")
class SensorMonitor:
    def __init__(self, threshold):
        self.threshold = threshold
        self.breached = False
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.breached:
            raise StopIteration
        value = random.uniform(0, 100)
        if value > self.threshold:
            self.breached = True
        return round(value, 2)

print("Sensor readings (threshold=90):")
for reading in SensorMonitor(90):
    print(reading)

# 5.4 Email validator
print("\n5.4 Email validator:")
import re
class EmailValidator:
    def __init__(self, emails):
        self.emails = emails
        self.index = 0
        self.pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self.index < len(self.emails):
            email = self.emails[self.index]
            self.index += 1
            if re.match(self.pattern, email):
                return email
        raise StopIteration

emails = ["valid@test.com", "invalid", "good@email.org"]
for valid in EmailValidator(emails):
    print(f"Valid: {valid}")

# 5.5 Low stock checker
print("\n5.5 Low stock checker:")
class LowStockAlert:
    def __init__(self, products, threshold):
        self.products = products
        self.threshold = threshold
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self.index < len(self.products):
            name, stock = self.products[self.index]
            self.index += 1
            if stock < self.threshold:
                return (name, stock)
        raise StopIteration

products = [("Shirt", 5), ("Pants", 2), ("Hat", 10)]
for alert in LowStockAlert(products, 3):
    print(f"Low stock: {alert[0]} ({alert[1]})")

print("\nAll 50 iterator exercises completed!")