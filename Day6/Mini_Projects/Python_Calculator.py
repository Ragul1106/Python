def calculator(a, b, operation):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Cannot divide by zero"
    }
    return operations[operation](a, b)

print("5 + 3 =", calculator(5, 3, '+'))
print("10 / 2 =", calculator(10, 2, '/'))