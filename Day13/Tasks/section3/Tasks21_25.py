  # Task 21: Create a Student class with private attributes _name and _marks. Use getter/setter methods.
class EncapsulatedStudent:
    def __init__(self, name, marks):
        self._name = name
        self._marks = marks

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks

# Task 22: Create a BankAccount class with balance as private variable. Ensure secure access via methods.
class SecureBankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Task 23: Build a UserProfile class with encapsulated email, phone and provide validation in setters.
class UserProfile:
    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

    def set_email(self, email):
        if "@" in email:
            self.__email = email

    def get_email(self):
        return self.__email

    def set_phone(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.__phone = phone

    def get_phone(self):
        return self.__phone

# Task 24: Restrict direct access to salary field in a class Employee, use getters/setters.
class SecureEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

    def get_salary(self):
        return self.__salary

# Task 25: Create a Locker system where the PIN is private and can only be changed via method.
class Locker:
    def __init__(self, pin):
        self.__pin = pin

    def change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin and len(str(new_pin)) == 4:
            self.__pin = new_pin
            return True
        return False