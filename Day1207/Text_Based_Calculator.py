history = []

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Cannot divide by zero"

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

while True:
    print("\nAvailable operations: +, -, *, /")
    print("Enter 'history' to view past calculations")
    print("Enter 'quit' to exit")
    
    choice = input("Enter operation: ")
    if choice.lower() == 'quit':
        break
    elif choice.lower() == 'history':
        print("\nCalculation History:")
        for h in history[-5:]:
            print(h)
        continue
    
    if choice not in operations:
        print("Invalid operation")
        continue
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = operations[choice](num1, num2)
        entry = f"{num1} {choice} {num2} = {result}"
        history.append(entry)
        print(entry)
    except ValueError:
        print("Invalid number input")