# Task 31: Demonstrate method overriding with Animal base class and Dog subclass implementing speak().
class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

# Task 32: Use polymorphism via duck typing – write a function that calls draw() on different shape objects.
class Circle:
    def draw(self):
        print("Drawing Circle")

class Square:
    def draw(self):
        print("Drawing Square")

def render(shape):
    shape.draw()

# Task 33: Simulate method overloading using default arguments in a class Calculator.
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Task 34: Simulate overloading using *args in a class Sum that can add 2, 3 or n numbers.
class Sum:
    def add(self, *args):
        return sum(args)

# Task 35: Create a class Notification with method send(msg). Use subclasses SMS, Email, PushNotification.
class Notification:
    def send(self, msg):
        print(f"Sending: {msg}")

class SMS(Notification):
    def send(self, msg):
        print(f"Sending SMS: {msg}")

class Email(Notification):
    def send(self, msg):
        print(f"Sending Email: {msg}")

class PushNotification(Notification):
    def send(self, msg):
        print(f"Sending Push Notification: {msg}")