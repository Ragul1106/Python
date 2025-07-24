import logging
from datetime import datetime

logging.basicConfig(filename='calculator.log', level=logging.ERROR)

class InvalidOperationError(Exception):
    pass

def smart_calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /, %): ")
        num2 = float(input("Enter second number: "))
        
        if op not in ['+', '-', '*', '/', '%']:
            raise InvalidOperationError("Invalid operator!")
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        elif op == '%':
            result = num1 % num2
            
    except ZeroDivisionError:
        error_msg = "Division by zero!"
        logging.error(f"{datetime.now()}: {error_msg}")
        print(error_msg)
    except ValueError:
        error_msg = "Invalid number input!"
        logging.error(f"{datetime.now()}: {error_msg}")
        print(error_msg)
    except InvalidOperationError as e:
        error_msg = str(e)
        logging.error(f"{datetime.now()}: {error_msg}")
        print(error_msg)
    else:
        print(f"Result: {result}")
    finally:
        print("Calculation complete")

smart_calculator()