import math

# Task 1: Create a Car class with attributes: brand, model, and price. Instantiate two cars and print details.
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"{self.brand} {self.model}: Rs.{self.price}")

car1 = Car("Toyota", "Camry", 3000000)
car2 = Car("Hyundai", "i20", 800000)
car1.display()
car2.display()

# Task 2: Create a BankAccount class with methods for deposit, withdraw, and balance check.
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def check_balance(self):
        return self.balance

# Task 3: Create a Student class with instance variables name, age, and grade. Accept data through the constructor.
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Task 4: Create a Circle class with method to calculate area and circumference.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Task 5: Create a Book class with display_info() method and access data via object.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"{self.title} by {self.author}")

# Task 6: Create a Laptop class with class variable warranty_period shared among all objects.
class Laptop:
    warranty_period = 1 

    def __init__(self, brand):
        self.brand = brand

# Task 7: Create a Movie class where each instance tracks the total number of movies using a class variable.
class Movie:
    total_movies = 0

    def __init__(self, title):
        self.title = title
        Movie.total_movies += 1

# Task 8: Create a Product class and demonstrate how instance variables differ from class variables.
class Product:
    category = "General"  

    def __init__(self, name):
        self.name = name  

# Task 9: Implement __str__ in a class Employee to display employee data in readable format.
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Employee Name: {self.name}, ID: {self.id}"

# Task 10: Write a program to compare two Rectangle objects using __eq__ method.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width