# Task 1: Print a greeting
print("Hello, Python!")

# Task 2: Print name and age in a single print statement
print("Ragul", 22)

# Task 3: Print fruits using sep
print("Apple", "Banana", "Grapes", sep=", ")

# Task 4: Print multiple texts on the same line using end
print("Python is fun", end=" ")
print("Python is fun", end=" ")
print("Python is fun")

# Task 5: Use f-string to print a number
print(f"My favorite number is {42}")

# Task 6: Print the result of addition
print(5 + 7)

# Task 7: Comment on print function
# print() is used to display text/output on the screen.

# Task 8: Use variable in print()
name = "Ragul"
print("Welcome", name)

# Task 9: Use sep to print fruits
print("Apple", "Banana", "Cherry", sep=" | ")

# Task 10: Print city and country in a single print using newline
print("Chennai\nIndia")

# Task 11: Create and print a string variable
name = "Ragul"
print(name)

# Task 12: Create and print an integer variable
age = 22
print(age)

# Task 13: Create and print a float variable
price = 49.99
print(price)

# Task 14: Create and print a boolean variable
is_student = True
print(is_student)

# Task 15: Create a list and print the second item
colors = ["Red", "Green", "Blue"]
print(colors[1])

# Task 16: Create and print values from a tuple
coordinates = (100, 200)
print(coordinates[0], coordinates[1])

# Task 17: Create and print dictionary values
car = {"brand": "Toyota", "year": 2020}
print(car["brand"], car["year"])

# Task 18: Create and print a set
nums = {10, 20, 30}
print(nums)

# Task 19: Reassign a variable and print before and after
msg = "Old"
print("Before:", msg)
msg = "New"
print("After:", msg)

# Task 20: Print the type of a string
x = "Hello"
print(type(x))

# Task 21: Assign and print an integer
a = 10
print(a)

# Task 22: Assign and print a float
b = 5.5
print(b)

# Task 23: Assign and print a string
quote = "Work hard in silence, let success make the noise."
print(quote)

# Task 24: Assign and print a boolean
flag = True
print(flag)

# Task 25: Print last item of list
subjects = ["Math", "English", "Science", "History", "CS"]
print(subjects[-1])

# Task 26: Print first city from tuple
cities = ("Paris", "London", "Rome")
print(cities[0])

# Task 27: Create and print dictionary
student = {"name": "Arun", "grade": "A"}
print(student)

# Task 28: Add duplicates to set and print
dup_set = {1, 1, 2, 3, 3}
print(dup_set)

# Task 29: Loop through list with mixed types and print type
mix = [10, "Hi", 3.5, False]
for val in mix:
    print(val, type(val))

# Task 30: Store string and print its type
val = "Python"
print(type(val))

# Task 31: Input name and greet
name = input("Enter your name: ")
print("Hello", name)

# Task 32: Input 2 numbers, add, and print
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)

# Task 33: Input age and print next year
age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1}")

# Task 34: Input color and print with f-string
color = input("Enter your favorite color: ")
print(f"{color} is beautiful!")

# Task 35: Input city and country and format message
city = input("City: ")
country = input("Country: ")
print(f"You live in {city}, {country}")

# Task 36: Input price and discount, print discounted price
price = float(input("Price: "))
discount = float(input("Discount: "))
final_price = price - discount
print(f"Discounted price: {final_price}")

# Task 37: Input 3 hobbies and print list
h1 = input("Hobby 1: ")
h2 = input("Hobby 2: ")
h3 = input("Hobby 3: ")
print("Your hobbies:", [h1, h2, h3])

# Task 38: Input name and age, print formatted
name = input("Enter name: ")
age = input("Enter age: ")
print(f"{name} is {age} years old.")

# Task 39: Input 2 numbers, multiply, and print with f-string
x = int(input("Num 1: "))
y = int(input("Num 2: "))
print(f"Product: {x * y}")

# Task 40: Input string and print its type
text = input("Enter something: ")
print("Type is:", type(text))

# Task 41: Create variable and print type
val = 100
print(type(val))

# Task 42: Use type() to check user input
user = input("Enter value: ")
print("Type:", type(user))

# Task 43: Convert input to int and show both types
snum = input("Enter a number as string: ")
inum = int(snum)
print("Before:", type(snum), "After:", type(inum))

# Task 44: Print each value and type from mixed list
mix_list = [1, "A", 2.2, False]
for item in mix_list:
    print(item, type(item))

# Task 45: Confirm True is bool
print(type(True))

# Task 46: Input year, convert to int, print type
birth = int(input("Enter birth year: "))
print("Type:", type(birth))

# Task 47: Create tuple and print type
tup = (1, 2, 3)
print(type(tup))

# Task 48: Create set and print type
s = {1, 2, 3}
print(s, type(s))

# Task 49: Print type of dictionary value
data = {"id": 101, "name": "Ragul"}
print(type(data["id"]))

# Task 50: Input string, print type, convert to float, print type
val = input("Enter a number: ")
print("Before:", type(val))
print("After:", type(float(val)))

