# 46. Build a calculator that uses exception handling for all basic operations
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        else:
            raise ValueError("Invalid operator!")
        
        print(f"Result: {result}")
    
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except ValueError as e:
        print(f"Error: {e}")

calculator()

# 47. Build a file copy tool that handles all common file errors
import shutil

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print("File copied successfully!")
    except FileNotFoundError:
        print("Error: Source file not found!")
    except PermissionError:
        print("Error: Permission denied!")
    except Exception as e:
        print(f"Error: {e}")

copy_file("source.txt", "destination.txt")

# 48. Build a user registration form that validates all fields and raises exceptions
class RegistrationError(Exception):
    pass

def register_user(username, password, email):
    if not username:
        raise RegistrationError("Username cannot be empty!")
    if len(password) < 8:
        raise RegistrationError("Password must be at least 8 characters!")
    if "@" not in email:
        raise RegistrationError("Invalid email format!")
    print("Registration successful!")

try:
    register_user("", "pass", "invalid-email")
except RegistrationError as e:
    print(f"Error: {e}")

# 49. Create an app that logs all exceptions to a file (using logging)
import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    logging.error(f"Error: {e}", exc_info=True)
    print("An error occurred. Check logs for details.")

# 50. Simulate a payment gateway that handles all input and system errors gracefully
class PaymentError(Exception):
    pass

def process_payment(amount, card_number):
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise PaymentError("Invalid amount!")
    if not str(card_number).isdigit() or len(str(card_number)) != 16:
        raise PaymentError("Invalid card number!")
    print(f"Processing payment of ${amount:.2f}...")
    
    
    import random
    if random.random() < 0.3:
        raise PaymentError("Payment failed due to network error!")
    print("Payment successful!")

try:
    process_payment(100, "1234567812345678")
except PaymentError as e:
    print(f"Payment Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")