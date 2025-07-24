# 11. Demonstrate try with else: divide numbers only if no exception
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input!")
else:
    print(f"Result: {result}")

# 12. Demonstrate try with finally: print "Done" regardless of error
try:
    num = int(input("Enter a number: "))
    print(f"Number: {num}")
except ValueError:
    print("Error: Invalid input!")
finally:
    print("Done")

# 13. Use multiple except blocks to catch ValueError and ZeroDivisionError
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input!")
except ZeroDivisionError:
    print("Error: Division by zero!")

# 14. Show that finally runs even when exception is raised and not caught
try:
    raise ValueError("Some error")
finally:
    print("Finally block executed")

# 15. Demonstrate combining else and finally together
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input!")
else:
    print(f"Number: {num}")
finally:
    print("Execution complete")

# 16. Handle exception in file reading and ensure file is closed using finally
file = None
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
finally:
    if file:
        file.close()

# 17. Nested try-except blocks: one inside another
try:
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError:
        print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input!")

# 18. Handle a situation where multiple types of exceptions might occur
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(my_list[num])
except (ValueError, ZeroDivisionError, IndexError) as e:
    print(f"Error: {e.__class__.__name__}")

# 19. Use except Exception as a generic fallback and explain it
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except Exception as e:  # Catches all exceptions (not recommended for production)
    print(f"An error occurred: {e}")

# 20. Demonstrate incorrect nesting of try-except-finally and correct it
# Incorrect
try:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Error: Invalid input!")
finally:
    print("Done")

# Correct
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input!")
finally:
    print("Done")