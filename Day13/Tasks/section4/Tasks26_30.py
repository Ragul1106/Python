from abc import ABC, abstractmethod

# Task 26: Use abc module to define an abstract class Payment with abstract method pay().
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using Credit Card")

# Task 27: Create an abstract class Shape with abstract method area() and concrete method describe().
class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a shape")

class Rectangle(AbstractShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Task 28: Implement Animal abstract class with abstract speak() method. Create subclasses Dog, Cat.
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

# Task 29: Create a template for Transport with abstract methods like start_engine() and stop_engine().
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Bus(Transport):
    def start_engine(self):
        print("Bus engine started")

    def stop_engine(self):
        print("Bus engine stopped")

# Task 30: Create a base class Appliance with abstract method power_consumption(). Subclasses: Fridge, WashingMachine.
class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass

class Fridge(Appliance):
    def power_consumption(self):
        return "150W"

class WashingMachine(Appliance):
    def power_consumption(self):
        return "500W"
