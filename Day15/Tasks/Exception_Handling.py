# 1. Divide two numbers, handle ZeroDivisionError and ValueError
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input! Please enter numbers.")

# 2. Take user input for age, raise error if non-numeric or negative
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Your age is: {age}")
except ValueError as e:
    print(f"Error: {e}")

# 3. Open a file, handle FileNotFoundError
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")

# 4. Read from a closed file, handle ValueError
file = open("example.txt", "w")
file.close()
try:
    file.read()
except ValueError:
    print("Error: File is closed!")

# 5. Handle IndexError when accessing list items by user input index
my_list = [1, 2, 3]
try:
    index = int(input("Enter index: "))
    print(f"Element: {my_list[index]}")
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Invalid index!")

# 6. Handle KeyError when accessing a dictionary with a missing key
my_dict = {"a": 1, "b": 2}
try:
    key = input("Enter key: ")
    print(f"Value: {my_dict[key]}")
except KeyError:
    print("Error: Key not found!")

# 7. Ask user to enter a number, convert to int, catch ValueError
try:
    num = int(input("Enter a number: "))
    print(f"Number: {num}")
except ValueError:
    print("Error: Invalid number!")

# 8. Catch TypeError when trying to add string and integer
try:
    result = "hello" + 5
except TypeError:
    print("Error: Cannot add string and integer!")

# 9. Catch AttributeError by calling a non-existent method on an object
class MyClass:
    pass

obj = MyClass()
try:
    obj.non_existent_method()
except AttributeError:
    print("Error: Method does not exist!")

# 10. Handle NameError when accessing an undefined variable
try:
    print(undefined_var)
except NameError:
    print("Error: Variable not defined!")