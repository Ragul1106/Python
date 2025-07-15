# Task 1: Create an empty tuple and print its type.
empty = ()
print(type(empty))

# Task 2: Create a tuple with integers, strings, and a float and print each item.
mix_tuple = (10, "hello", 3.14)
for item in mix_tuple:
    print(item)

# Task 3: Create a tuple with only one element and print its type.
single = (5,)
print(type(single))

# Task 4: Convert a list to a tuple.
nums = [1, 2, 3, 4, 5]
tuple_nums = tuple(nums)
print(tuple_nums)

# Task 5: Convert a string to a tuple of characters.
text = "Python"
char_tuple = tuple(text)
print(char_tuple)

# Task 6: Access the first and last elements of a tuple.
t = (10, 20, 30, 40, 50)
print(t[0], t[-1])

# Task 7: Slice a tuple to get the middle 3 elements.
print(t[1:4])

# Task 8: Reverse a tuple using slicing.
print(t[::-1])

# Task 9: Access every second element.
print(t[::2])

# Task 10: Get a sub-tuple using negative indexing.
print(t[-4:-1])

# Task 11: Attempt to change a tuple element (will raise error).
try:
    t[0] = 99
except TypeError as e:
    print(e)

# Task 12: Replace value by converting to list and back.
temp = list(t)
temp[0] = 99
t = tuple(temp)
print(t)

# Task 13: Add a new value via concatenation.
t += (60,)
print(t)

# Task 14: Remove an item via conversion to list.
temp = list(t)
temp.remove(60)
t = tuple(temp)
print(t)

# Task 15: Demonstrate partial deletion fails.
try:
    del t[0]
except TypeError as e:
    print(e)

# Task 16: Concatenate tuples.
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# Task 17: Repeat tuple.
print(t1 * 3)

# Task 18: Check item existence.
print(2 in t1)

# Task 19: Find length.
print(len(t1))

# Task 20: Count occurrence.
t = (1, 2, 3, 1, 1)
print(t.count(1))

# Task 21: count()
print(t.count(2))

# Task 22: index()
print(t.index(3))

# Task 23: max() and min()
print(max(t), min(t))

# Task 24: sum()
print(sum(t))

# Task 25: sorted()
print(sorted(t))

# Task 26: For loop
for val in t:
    print(val)

# Task 27: enumerate()
for i, val in enumerate(t):
    print(i, val)

# Task 28: While loop
i = 0
while i < len(t):
    print(t[i])
    i += 1

# Task 29: Even numbers
for val in t:
    if val % 2 == 0:
        print(val)

# Task 30: Count strings starting with 'A'
names = ("Alice", "Bob", "Angela", "Steve")
count = 0
for name in names:
    if name.startswith("A"):
        count += 1
print(count)

# Task 31: Create and access inner elements
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1][1])

# Task 32: Print all sub-tuples
for sub in nested:
    print(sub)

# Task 33: Sum all nested numbers
total = 0
for sub in nested:
    total += sum(sub)
print(total)

# Task 34: Flatten nested tuple
flat = []
for sub in nested:
    flat.extend(sub)
print(tuple(flat))

# Task 35: Access second of third sub-tuple
print(nested[2][1])

# Task 36: Packing
packed = 1, 2, 3
print(packed)

# Task 37: Unpacking
x, y, z = packed
print(x, y, z)

# Task 38: Swap using unpacking
a, b = 5, 10
a, b = b, a
print(a, b)

# Task 39: Use * to unpack remaining
first, *rest = (1, 2, 3, 4)
print(first, rest)

# Task 40: Unpack nested tuples
nested2 = ("John", (90, 95))
name, (m1, m2) = nested2
print(name, m1, m2)

# Task 41: Return multiple values as tuple
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)
print(stats((10, 20, 30)))

# Task 42: Pass tuple to function
def show(tup):
    for i in tup:
        print(i)
show((1, 2, 3))

# Task 43: Average from tuple input
def average(t):
    return sum(t)/len(t)
print(average((10, 20, 30)))

# Task 44: Min & Max from tuple
def min_max(t):
    return min(t), max(t)
print(min_max((1, 5, 2)))

# Task 45: Merge two tuples
def merge(t1, t2):
    return t1 + t2
print(merge((1, 2), (3, 4)))

# Task 46: Store coordinates
location = (12.9716, 77.5946)
print(f"Latitude: {location[0]}, Longitude: {location[1]}")

# Task 47: Phonebook
phonebook = [("Alice", "1234"), ("Bob", "5678")]
for name, number in phonebook:
    print(name, number)

# Task 48: RGB values
pixel = (255, 128, 0)
print(f"Red: {pixel[0]}, Green: {pixel[1]}, Blue: {pixel[2]}")

# Task 49: Exam results
results = [("Alice", 88), ("Bob", 92), ("Charlie", 85)]
top = max(results, key=lambda x: x[1])
print(f"Top Scorer: {top[0]} with {top[1]}")

# Task 50: Immutable config
config = ("localhost", 8080, False)
print(f"Host: {config[0]}, Port: {config[1]}, Debug: {config[2]}")