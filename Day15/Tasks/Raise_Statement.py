# 21. Raise ValueError manually if user enters a negative number
num = int(input("Enter a positive number: "))
if num < 0:
    raise ValueError("Number must be positive!")

# 22. Raise TypeError if function argument is not a string
def greet(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string!")
    print(f"Hello, {name}")

greet(123)  

# 23. Create a function that only accepts positive integers, use raise
def process_positive(num):
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Number must be a positive integer!")
    print(f"Processing: {num}")

process_positive(-5)  

# 24. Simulate a login system and raise exception if password is incorrect
def login(username, password):
    if password != "secret":
        raise ValueError("Incorrect password!")
    print("Login successful")

login("user", "wrong")  

# 25. Raise an error if a required key is missing from a dictionary
data = {"name": "Alice"}
required_key = "age"
if required_key not in data:
    raise KeyError(f"Missing required key: {required_key}")

# 26. Raise a ZeroDivisionError with custom error message
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

divide(10, 0)  

# 27. Use assert to raise error if number is not even
num = int(input("Enter an even number: "))
assert num % 2 == 0, "Number must be even!"

# 28. Validate email format and raise a ValueError if invalid
import re
def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format!")
    print("Email is valid")

validate_email("invalid-email")  

# 29. Raise an exception if list is empty before processing
my_list = []
if not my_list:
    raise ValueError("List is empty!")

# 30. Raise error if file is empty before reading
import os
filename = "empty.txt"
if os.path.getsize(filename) == 0:
    raise ValueError("File is empty!")