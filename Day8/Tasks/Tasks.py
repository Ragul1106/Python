# Task 1: Create a list of 5 student names and print it.
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
print(students)

# Task 2: Create a list with mixed data types and display each element.
mixed = [10, 3.14, "hello", True]
for item in mixed:
    print(item)

# Task 3: Accept 5 numbers from the user and store them in a list.
numbers = []
for _ in range(5):
    numbers.append(int(input("Enter a number: ")))
print(numbers)

# Task 4: Create an empty list and append 3 user inputs.
inputs = []
for _ in range(3):
    inputs.append(input("Enter value: "))
print(inputs)

# Task 5: Create a list of 10 even numbers using a for loop.
evens = [i for i in range(2, 21, 2)]
print(evens)

# Task 6: Create two lists and print them together.
ints = [1, 2, 3]
strings = ["one", "two", "three"]
print(ints + strings)

# Task 7: Print only the first and last items of a fruit list.
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0], fruits[-1])

# Task 8: Use negative indexing to print the second-last item.
print(fruits[-2])

# Task 9: Count total number of elements in a list using len().
print(len(fruits))

# Task 10: Check the data type of a list.
print(type(fruits))

# Task 11: Access and print each element using for loop with indexing.
for i in range(len(fruits)):
    print(fruits[i])

# Task 12: Print every alternate item from a list.
print(fruits[::2])

# Task 13: Create city list and print 3rd char of 2nd city.
cities = ["Mumbai", "Chennai", "Delhi"]
print(cities[1][2])

# Task 14: Reverse a list using slicing.
print(fruits[::-1])

# Task 15: Access last element using positive and negative index.
print(fruits[3], fruits[-1])

# Task 16: Use append() to add 5 elements.
data = []
for i in range(5):
    data.append(i)
print(data)

# Task 17: Insert element at 3rd position.
data.insert(2, 99)
print(data)

# Task 18: Use extend() to add multiple elements.
data.extend([100, 200])
print(data)

# Task 19: Take name input and add to student list.
name = input("Enter a student name: ")
students.append(name)
print(students)

# Task 20: Add elements from one list into another.
data += [300, 400]
data.extend([500])
print(data)

# Task 21: Change first element to uppercase.
students[0] = students[0].upper()
print(students)

# Task 22: Modify product price.
prices = [100, 200, 300, 400]
prices[2] = 999
print(prices)

# Task 23: Multiply all odd numbers by 2.
numbers = [1, 2, 3, 4, 5]
numbers = [x * 2 if x % 2 != 0 else x for x in numbers]
print(numbers)

# Task 24: Replace fruit with new one.
fruits[1] = "grape"
print(fruits)

# Task 25: Update nested list item.
nested = [[1, 2, 3], [4, 5, 6]]
nested[1][2] = 'done'
print(nested)

# Task 26: Remove specific value.
fruits.remove("grape")
print(fruits)

# Task 27: Pop last item.
fruits.pop()
print(fruits)

# Task 28: Pop index 2.
prices.pop(2)
print(prices)

# Task 29: Del index 3.
del prices[2]
print(prices)

# Task 30: Clear list.
prices.clear()
print(prices)

# Task 31: Print all in uppercase.
for fruit in fruits:
    print(fruit.upper())

# Task 32: Find and print odd numbers.
for num in numbers:
    if num % 2 != 0:
        print(num)

# Task 33: Print square of numbers.
for num in numbers:
    print(num ** 2)

# Task 34: Use enumerate().
for index, value in enumerate(fruits):
    print(index, value)

# Task 35: Count how many times 'apple'.
apples = ["apple", "banana", "apple", "apple"]
count = 0
for item in apples:
    if item == "apple":
        count += 1
print(count)

# Task 36: Create nested list.
students_data = [["John", 85], ["Sara", 90]]
print(students_data)

# Task 37: Print name of 2nd student.
print(students_data[1][0])

# Task 38: Update marks.
students_data[0][1] = 95
print(students_data)

# Task 39: Iterate over nested list.
for student in students_data:
    print(f"Name: {student[0]}, Marks: {student[1]}")

# Task 40: Add new student.
students_data.append(["Mike", 88])
print(students_data)

# Task 41: Concatenate lists.
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)

# Task 42: Repeat list 3 times.
print(["Hi"] * 3)

# Task 43: Slice first 3.
print(l1[:3])

# Task 44: Slice all except first & last.
print(l1[1:-1])

# Task 45: Merge list of numbers with strings.
combined = l1 + ["one", "two"]
print(combined)

# Task 46: Check fruit in list.
fruit_input = input("Enter fruit name: ")
print(fruit_input in fruits)

# Task 47: Remove only if exists.
if "banana" in fruits:
    fruits.remove("banana")
print(fruits)

# Task 48: Count specific element.
print(apples.count("apple"))

# Task 49: Check if number in marks.
marks = [50, 60, 70, 80]
num = int(input("Enter a number: "))
print(num in marks)

# Task 50: Ask and check item presence.
item = input("Enter an item: ")
print("Present" if item in fruits else "Not Present")
