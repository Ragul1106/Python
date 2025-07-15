# Task 1: Create a dictionary with five employee names and their ID numbers.
employees = {"John": 101, "Alice": 102, "Bob": 103, "Eve": 104, "Sam": 105}
print(employees)

# Task 2: Access and print the phone number from a contact dictionary.
contacts = {"Ravi": "9876543210"}
print(contacts["Ravi"])

# Task 3: Use the get() method to retrieve a value that may not exist.
print(contacts.get("Sita", "Not Found"))

# Task 4: Add a new key-value pair to a student marks dictionary.
marks = {"Ravi": 88}
marks["Sita"] = 92
print(marks)

# Task 5: Update an existing student's score.
marks["Ravi"] = 90
print(marks)

# Task 6: Delete a key using del.
del marks["Ravi"]
print(marks)

# Task 7: Use pop() to remove a key and display the value.
removed = marks.pop("Sita")
print("Removed value:", removed)

# Task 8: Use popitem().
user_info = {"name": "Rahul", "age": 25}
print(user_info.popitem())

# Task 9: Clear all entries.
user_info.clear()
print(user_info)

# Task 10: Check if a key exists.
print("Ravi" in marks)

# Task 11: Loop and print all keys.
for key in employees:
    print(key)

# Task 12: Loop and print all values.
for value in employees.values():
    print(value)

# Task 13: Loop through keys and values.
for k, v in employees.items():
    print(k, v)

# Task 14: Count values > 90.
grades = {"A": 91, "B": 89, "C": 95}
print(len([v for v in grades.values() if v > 90]))

# Task 15: Return all keys with a specific value.
def keys_with_value(d, val):
    return [k for k, v in d.items() if v == val]
print(keys_with_value(grades, 95))

# Task 16: Merge two dicts.
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
print(d1)

# Task 17: Use setdefault().
d1.setdefault("c", 3)
print(d1)

# Task 18: Copy dict.
copy_d1 = d1.copy()
d1["a"] = 100
print("Original:", d1, "Copy:", copy_d1)

# Task 19: Create dict from list of tuples.
pair_list = [("x", 10), ("y", 20)]
pair_dict = dict(pair_list)
print(pair_dict)

# Task 20: Get keys and values.
print(pair_dict.keys())
print(pair_dict.values())

# Task 21: Shopping cart.
cart = {"apple": 2, "banana": 3}
print(cart)

# Task 22: Grade book.
gradebook = {"John": "A", "Sara": "B"}
print(gradebook)

# Task 23: Phonebook.
phonebook = {"Ravi": "9999999999"}
print(phonebook.get("Ravi"))

# Task 24: Product inventory.
inventory = {101: {"name": "Pen", "stock": 50}}
print(inventory[101])

# Task 25: Attendance tracker.
attendance = {"2023-07-01": ["Ravi", "Sara"]}
print(attendance)

# Task 26: Nested employee dict.
employees_data = {101: {"name": "John", "salary": 50000}}
print(employees_data)

# Task 27: Access nested value.
print(employees_data[101]["name"])

# Task 28: Add new employee.
employees_data[102] = {"name": "Sara", "salary": 60000}
print(employees_data)

# Task 29: Update salary.
employees_data[101]["salary"] = 55000
print(employees_data)

# Task 30: Loop through nested dict.
for emp in employees_data.values():
    print(emp["name"], emp["salary"])

# Task 31: Squares.
squares = {n: n**2 for n in range(1, 6)}
print(squares)

# Task 32: Even/odd.
nums = [1, 2, 3, 4, 5]
even_odd = {n: "even" if n % 2 == 0 else "odd" for n in nums}
print(even_odd)

# Task 33: Word lengths.
words = ["hello", "world"]
lengths = {w: len(w) for w in words}
print(lengths)

# Task 34: Swap keys/values.
swapped = {v: k for k, v in lengths.items()}
print(swapped)

# Task 35: Filter dict.
filtered = {k: v for k, v in grades.items() if v > 90}
print(filtered)

# Task 36: Char frequency.
text = "hello"
char_freq = {}
for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1
print(char_freq)

# Task 37: Word count.
para = "this is a test this is only a test"
word_count = {}
for word in para.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Task 38: Fruit prices.
fruits = {"apple": 50, "banana": 20, "cherry": 80}
print(max(fruits, key=fruits.get))

# Task 39: Total inventory.
prices = {"pen": 10, "book": 50}
quantities = {"pen": 3, "book": 2}
total_value = sum(prices[item] * quantities[item] for item in prices)
print(total_value)

# Task 40: Group students.
students = [("John", "A"), ("Sara", "B"), ("Alex", "A")]
grouped = {}
for name, grade in students:
    grouped.setdefault(grade, []).append(name)
print(grouped)

# Task 41: Caching system.
cache = {}
def factorial(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = n * factorial(n-1)
    return cache[n]
print(factorial(5))

# Task 42: URL shortener.
shortener = {"abc": "https://google.com"}
print(shortener.get("abc"))

# Task 43: Translator.
dictionary = {"hello": "வணக்கம்"}
print(dictionary.get("hello"))

# Task 44: Login system.
users = {"admin": "pass123"}
username = "admin"
password = "pass123"
print("Login Success" if users.get(username) == password else "Failed")

# Task 45: Movie manager.
movies = {"Inception": (2010, "Sci-Fi")}
print(movies["Inception"])

# Task 46: Calculator using dict.
calc = {"+": lambda a, b: a + b, "-": lambda a, b: a - b}
print(calc["+"](10, 5))

# Task 47: Travel expense.
expenses = {"Chennai": 5000, "Delhi": 8000}
print(expenses)

# Task 48: File extension counter.
files = ["a.txt", "b.jpg", "c.txt"]
count = {}
for f in files:
    ext = f.split(".")[-1]
    count[ext] = count.get(ext, 0) + 1
print(count)

# Task 49: Country capitals.
capitals = {"India": "Delhi", "Japan": "Tokyo"}
print(capitals.get("India"))

# Task 50: Quiz app.
quiz = {"Capital of India?": "Delhi"}
for q, a in quiz.items():
    ans = input(q + " ")
    print("Correct!" if ans == a else "Wrong!")
