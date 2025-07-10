def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

print(f"Factorial of 5: {factorial(5)}")
print(f"8th Fibonacci number: {fibonacci(8)}")