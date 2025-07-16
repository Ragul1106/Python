# Task 1: Create a set of favorite fruits and print it.
fav_fruits = {"apple", "banana", "mango"}
print(fav_fruits)

# Task 2: Convert a list with duplicate values into a unique set.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

# Task 3: Check if a given item exists in a set.
print("apple" in fav_fruits)

# Task 4: Create a set from a string and print unique characters.
char_set = set("hello world")
print(char_set)

# Task 5: Iterate through a set and print each element.
for fruit in fav_fruits:
    print(fruit)

# Task 6: Add five movie names using add().
movies = set()
for m in ["Inception", "Titanic", "Avatar", "Joker", "Tenet"]:
    movies.add(m)
print(movies)

# Task 7: Add multiple subjects using update().
subjects = {"Math"}
subjects.update(["Science", "English", "History"])
print(subjects)

# Task 8: Add multiple letters from a string using update().
letters = set()
letters.update("hello")
print(letters)

# Task 9: Remove a city.
cities = {"Delhi", "Mumbai", "Chennai"}
cities.remove("Delhi")
print(cities)

# Task 10: Discard an element safely.
cities.discard("Hyderabad")
print(cities)

# Task 11: Remove random item using pop().
removed = cities.pop()
print("Removed:", removed)
print(cities)

# Task 12: Clear the set.
cities.clear()
print(cities)

# Task 13: Union of two sets.
a = {"Python", "Java"}
b = {"C++", "Java"}
print(a | b)

# Task 14: Intersection
print(a & b)

# Task 15: Difference (A - B)
print(a - b)

# Task 16: Symmetric difference
print(a ^ b)

# Task 17: Chained operation
print((a | b) - (a & b))

# Task 18: Subset
backend = {"Python", "Django"}
fullstack = {"HTML", "CSS", "Python", "Django"}
print(backend.issubset(fullstack))

# Task 19: Superset
developers = {"Alice", "Bob", "Charlie"}
testers = {"Bob"}
print(developers.issuperset(testers))

# Task 20: Disjoint
colors1 = {"red", "blue"}
colors2 = {"green", "yellow"}
print(colors1.isdisjoint(colors2))

# Task 21: Multiple set comparisons
print(backend <= fullstack, fullstack >= backend)

# Task 22: Course completion
required = {"Module1", "Module2"}
completed = {"Module1", "Module2", "Module3"}
print(required.issubset(completed))

# Task 23: Copy and modify
orig = {1, 2, 3}
backup = orig.copy()
backup.add(4)
print("Original:", orig)
print("Backup:", backup)

# Task 24: Create frozenset
vowels = frozenset("aeiou")
print(vowels)

# Task 25: Try adding to frozenset
try:
    vowels.add("z")
except AttributeError as e:
    print("Error:", e)

# Task 26: Use frozenset as key
cache = {frozenset([1, 2]): "cached result"}
print(cache[frozenset([2, 1])])

# Task 27: Even numbers
evens = {x for x in range(1, 21) if x % 2 == 0}
print(evens)

# Task 28: Unique lowercase chars
sentence = "Hello Python World"
lowercase = {c.lower() for c in sentence if c.isalpha()}
print(lowercase)

# Task 29: Squares
squares = {x ** 2 for x in range(1, 11)}
print(squares)

# Task 30: Filter vowels from sentence
filtered = {c for c in sentence.lower() if c not in "aeiou" and c.isalpha()}
print(filtered)

# Task 31: Allowed users
registered = {"user1", "user2", "user3"}
blocked = {"user2"}
allowed = registered - blocked
print(allowed)

# Task 32: Common students
python = {"A", "B", "C"}
java = {"B", "C", "D"}
print(python & java)

# Task 33: New listings
old = {"AAPL", "GOOG"}
new = {"GOOG", "TSLA"}
print(new - old)

# Task 34: Union of login users
yesterday = {"user1", "user3"}
today = {"user2", "user3"}
print(yesterday | today)

# Task 35: Password change only one day
print(yesterday ^ today)

# Task 36: Detect duplicates
skus = ["A1", "A2", "A1", "B1"]
print(len(set(skus)) != len(skus))

# Task 37: Unique from CSV column
csv_column = ["apple", "banana", "apple", "orange"]
print(set(csv_column))

# Task 38: Tag manager
tags = set()
tags.update(["tech", "python", "ai"])
print(tags)

# Task 39: Permissions check
required_perms = {"read", "write"}
default_perms = {"read", "write", "execute"}
print(required_perms.issubset(default_perms))

# Task 40: Random number sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)

# Task 41: Contact manager
emails = set(["a@example.com", "b@example.com"])
emails.add("c@example.com")
print(emails)

# Task 42: Achievements
players = {"Trophy1", "Trophy2"}
majors = {"Trophy1", "Trophy2", "Trophy3"}
print(players.issuperset(majors))

# Task 43: Unique IPs
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.1"]
print(set(ips))

# Task 44: Unique hashtags
tweets = ["#fun", "#python", "#fun"]
print(set(tweets))

# Task 45: Unique book titles
lib1 = {"Book1", "Book2"}
lib2 = {"Book3"}
lib1.update(lib2)
print(lib1)

# Task 46: Module check
installed = {"numpy", "pandas", "matplotlib"}
required = {"numpy", "pandas"}
print(required.issubset(installed))

# Task 47: Remove with exception
try:
    subjects.remove("Geography")
except KeyError:
    print("Not Found")

# Task 48: Remove vs discard
sample = {1, 2, 3}
sample.discard(5)  # no error
try:
    sample.remove(5)
except KeyError:
    print("Remove failed")

# Task 49: Mixed data types
mixed = {1, "two", 3.0, True}
filtered = {x for x in mixed if not isinstance(x, int)}
print(filtered)

# Task 50: Exclude punctuation
text = "Hello, World! Python."
chars = {c for c in text if c.isalpha()}
print(chars)
