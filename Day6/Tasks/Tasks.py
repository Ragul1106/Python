# Task 1: Define a function greet() that prints “Welcome to Python!”.
def greet():
    print("Welcome to Python!")

# Task 2: Write a function add(a, b) that returns the sum of two numbers.
def add(a, b):
    return a + b

# Task 3: Define a function is_even(num) that returns True if the number is even.
def is_even(num):
    return num % 2 == 0

# Task 4: Create a function cube(n) that returns the cube of a number.
def cube(n):
    return n ** 3

# Task 5: Write a function hello(name) that prints "Hello, <name>".
def hello(name):
    print(f"Hello, {name}")

# Task 6: Define a function with no code yet using pass.
def future_function():
    pass

# Task 7: Create a function that takes two numbers and prints which is greater using if.
def compare_numbers(a, b):
    if a > b:
        print(f"{a} is greater")
    elif b > a:
        print(f"{b} is greater")
    else:
        print("Both are equal")

# Task 8: Write a function square_area(side) to return the area of a square.
def square_area(side):
    return side * side

# Task 9: Create a menu-based function with options (view, add, exit) using if-else.
def menu_app(option):
    if option == "view":
        print("Viewing items...")
    elif option == "add":
        print("Adding item...")
    elif option == "exit":
        print("Exiting...")
    else:
        print("Invalid option")

# Task 10: Call a function multiple times in a loop to show reusability.
def call_multiple():
    for _ in range(3):
        greet()


# Task 11: Define a function divide(a, b) and return the quotient. Handle divide-by-zero.
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Task 12: Create a function full_name(fname, lname) that returns a full name.
def full_name(fname, lname):
    return f"{fname} {lname}"

# Task 13: Write a function that takes age as input and returns if the user is eligible to vote.
def vote_eligibility(age):
    return age >= 18

# Task 14: Create a function calc_discount(price, discount_percent) that returns the final price.
def calc_discount(price, discount_percent):
    return price - (price * discount_percent / 100)

# Task 15: Write a function to calculate and return the average of 3 numbers.
def average_of_three(n1, n2, n3):
    return (n1 + n2 + n3) / 3


# Task 16: Create a global variable x = 100, and print it inside a function.
x = 100
def print_global():
    print(x)

# Task 17: Create a function with a local variable and show that it's not accessible outside.
def local_variable():
    message = "This is local"
    print(message)

# Task 18: Use both a global and a local variable in the same function and print both.
y = 200
def global_local():
    z = 300
    print(f"Global y: {y}, Local z: {z}")

# Task 19: Modify a global variable inside a function using the global keyword.
a = 10
def modify_global():
    global a
    a = 50

# Task 20: Show that a variable with the same name inside a function doesn’t affect the global one.
b = "global value"
def shadow_variable():
    b = "local value"
    print("Inside function:", b)


# Task 21: Write a recursive function to calculate factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Task 22: Create a recursive function to calculate the nth Fibonacci number.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Task 23: Use recursion to reverse a string.
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

# Task 24: Use recursion to sum all elements in a list.
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

# Task 25: Write a recursive function that counts down from a number to 1.
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)


# Task 26: Write a function add_numbers(*args) that returns the sum of all arguments.
def add_numbers(*args):
    return sum(args)

# Task 27: Create a function that prints all positional arguments received via *args.
def print_args(*args):
    for arg in args:
        print(arg)

# Task 28: Create a function student_info(**kwargs) to print student data.
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Task 29: Combine *args and **kwargs in one function and display both.
def combine_args_kwargs(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

# Task 30: Write a function that accepts an unknown number of keyword arguments and filters only those with integer values.
def filter_integers(**kwargs):
    return {k: v for k, v in kwargs.items() if isinstance(v, int)}


# Task 31: Write a lambda function to add two numbers.
add_lambda = lambda a, b: a + b

# Task 32: Create a lambda to return the square of a number.
square = lambda x: x ** 2

# Task 33: Use lambda with sorted() to sort a list of tuples by second value.
tuple_list = [("a", 3), ("b", 1), ("c", 2)]
sorted_list = sorted(tuple_list, key=lambda x: x[1])

# Task 34: Replace a normal function with a lambda version.
cube_lambda = lambda x: x ** 3

# Task 35: Use a lambda function inside another function (function returning lambda).
def multiplier(n):
    return lambda x: x * n


from functools import reduce

# Task 36: Use map() and lambda to square every element in a list.
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))

# Task 37: Use filter() to remove all odd numbers from a list.
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Task 38: Use map() to convert a list of strings to uppercase.
words = ["hello", "world"]
uppercase = list(map(str.upper, words))

# Task 39: Use reduce() to calculate the product of a list.
product = reduce(lambda x, y: x * y, numbers)

# Task 40: Use filter() to return words longer than 5 characters from a list.
word_list = ["apple", "banana", "pineapple"]
long_words = list(filter(lambda w: len(w) > 5, word_list))


# Task 41: Assign a function to a variable and call it using the new name.
def shout():
    return "Hello!"
shout_alias = shout

# Task 42: Create a function that takes another function as an argument.
def call_func(func):
    print(func())

# Task 43: Write a function that returns another function.
def outer():
    def inner():
        return "Inner function called"
    return inner

# Task 44: Pass a lambda function as an argument to another function.
def apply_func(f, x):
    return f(x)

# Task 45: Write a function that takes two numbers and a function (like add, subtract) and applies it.
def compute(a, b, func):
    return func(a, b)


# Task 46: Write a function with a nested function inside that prints a message.
def outer_message():
    def inner():
        print("Nested Hello!")
    inner()

# Task 47: Write a function that uses an inner function to double a number, and return the result.
def double_number(n):
    def doubler(x):
        return x * 2
    return doubler(n)


# Task 48: Create a class Person with attributes and a method greet() that uses self.
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I am {self.name}"

# Task 49: Create a class Calculator with methods add, subtract, using self.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


# Task 50: Create a billing app with functions: add_item(name, price), get_total(), apply_discount(percent)
bill_items = []

def add_item(name, price):
    bill_items.append((name, price))

def get_total():
    return sum(price for name, price in bill_items)

def apply_discount(percent):
    return get_total() * (1 - percent / 100)
