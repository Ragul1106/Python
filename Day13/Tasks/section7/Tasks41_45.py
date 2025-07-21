# Task 41: Create a Car class that contains an Engine object (composition).
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start(self):
        print(f"Starting {self.brand} car.")
        self.engine.start()

# Task 42: Design a Library class that has a list of Book objects (aggregation).
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

# Task 43: Create a University class containing multiple Department objects (composition).
class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self):
        self.departments = []

    def add_department(self, dept):
        self.departments.append(dept)

# Task 44: Build a Company object that aggregates many Employee instances.
class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

# Task 45: Create a Flight object that includes Pilot, CabinCrew, and Passenger classes.
class Pilot:
    def __init__(self, name):
        self.name = name

class CabinCrew:
    def __init__(self, name):
        self.name = name

class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, pilot, crew, passengers):
        self.pilot = pilot
        self.crew = crew
        self.passengers = passengers
