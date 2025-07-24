# 41. Ask user to enter 5 valid integers using a loop, handle bad inputs
valid_numbers = []
while len(valid_numbers) < 5:
    try:
        num = int(input(f"Enter number {len(valid_numbers) + 1}: "))
        valid_numbers.append(num)
    except ValueError:
        print("Error: Invalid input!")

print("Valid numbers:", valid_numbers)

# 42. Write a function that opens and reads file and handles any error
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found!"
    except IOError:
        return "Error: Could not read file!"

print(read_file("example.txt"))

# 43. Handle exception in recursive function (e.g., factorial)
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer!")
    return 1 if n == 0 else n * factorial(n - 1)

try:
    print(factorial(-5))
except ValueError as e:
    print(f"Error: {e}")

# 44. Inside a loop, catch and skip bad inputs instead of crashing
numbers = ["1", "2", "abc", "3"]
valid = []
for num in numbers:
    try:
        valid.append(int(num))
    except ValueError:
        continue
print("Valid numbers:", valid)

# 45. Demonstrate try-except inside a list comprehension (with filtering)
data = ["1", "2", "abc", "3"]
valid_numbers = [int(x) for x in data if x.isdigit()]
print("Valid numbers:", valid_numbers)