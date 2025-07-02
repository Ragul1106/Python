num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Enter operation (add/subtract/multiply/divide): ")

print(f"\nnum1 type: {type(num1)}")
print(f"num2 type: {type(num2)}")
print(f"operation type: {type(operation)}")

num1 = float(num1)
num2 = float(num2)

if operation == 'add':
    result = num1 + num2
elif operation == 'subtract':
    result = num1 - num2
elif operation == 'multiply':
    result = num1 * num2
elif operation == 'divide':
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"\nResult: {result}")
print(f"Result type: {type(result)}")