# Task 46: Design a BankAccount class with deposit, withdraw, and check_balance methods.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance

# Task 47: Implement a School Management System with Student and Teacher classes.
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

# Task 48: Build a Hospital Management System with Doctor, Patient, and Appointment.
class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

class Patient:
    def __init__(self, name, illness):
        self.name = name
        self.illness = illness

class Appointment:
    def __init__(self, doctor, patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date

# Task 49: Implement a Library System with Members and Lending functionality.
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def add_book(self, book):
        self.books.append(book)

# Task 50: Create an E-commerce system with Product, Customer, and Order classes.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = customer.cart

    def total(self):
        return sum(item.price for item in self.items)