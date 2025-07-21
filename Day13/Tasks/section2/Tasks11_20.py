# Task 11: Create a Vehicle class and inherit it in Car, Bike, and Truck classes.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

# Task 12: Use super() to call the parent class constructor from a child class.

# Task 13: Create a Shape class and derive Square and Triangle. Override an area() method.
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Task 14: Implement Multi-level Inheritance with Person → Employee → Manager.
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, eid):
        super().__init__(name)
        self.eid = eid

class Manager(Employee):
    def __init__(self, name, eid, level):
        super().__init__(name, eid)
        self.level = level

# Task 15: Demonstrate Multiple Inheritance with Father and Mother inherited by Child.
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

# Task 16: Create a Teacher class and use hierarchical inheritance for MathTeacher, ScienceTeacher.
class Teacher:
    def teach(self):
        print("Teaching")

class MathTeacher(Teacher):
    pass

class ScienceTeacher(Teacher):
    pass

# Task 17: Use isinstance() to check if an object belongs to a certain class.
teacher = MathTeacher()
print(isinstance(teacher, Teacher))  # True

# Task 18: Use issubclass() to verify if a class is derived from another class.
print(issubclass(ScienceTeacher, Teacher))  # True

# Task 19: Create a class hierarchy for an e-commerce platform using inheritance (Product → ElectronicProduct → MobilePhone).
class Product:
    def __init__(self, name):
        self.name = name

class ElectronicProduct(Product):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

class MobilePhone(ElectronicProduct):
    def __init__(self, name, brand, model):
        super().__init__(name, brand)
        self.model = model

# Task 20: Demonstrate method resolution order (MRO) in a multiple inheritance example.
class A:
    def process(self):
        print("A")

class B(A):
    def process(self):
        print("B")

class C(A):
    def process(self):
        print("C")

class D(B, C):
    pass

d = D()
d.process()