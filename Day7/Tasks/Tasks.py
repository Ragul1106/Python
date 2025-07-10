# Task 1: Create a string using single, double, and triple quotes
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''Welcome to Python'''

# Task 2: Create a multiline quote using triple quotes and print it
multiline = '''This is a multiline
string using triple quotes.'''
print(multiline)

# Task 3: Access first and last character from string
s = "Python"
print(s[0])  # First
print(s[-1]) # Last

# Task 4: Print every character using for loop
for char in s:
    print(char)

# Task 5: Slice middle 3 characters
mid = len(s) // 2
print(s[mid-1:mid+2])

# Task 6: Access every second character
print(s[::2])

# Task 7: Print all vowels from string
for ch in s:
    if ch.lower() in 'aeiou':
        print(ch)

# Task 8: Extract domain from email
email = "user@gmail.com"
domain = email[email.find('@')+1:]
print(domain)

# Task 9: Check if first and last characters are the same
print(s[0] == s[-1])

# Task 10: Reverse the string using slicing
print(s[::-1])


# Task 11: Try modifying string (will raise error)
s[0] = "J"  # ❌ Not allowed

# Task 12: Change first character using slicing
s = "hello"
s = "H" + s[1:]
print(s)

# Task 13: Replace character in middle by reconstructing
s = "hello"
s = s[:2] + "X" + s[3:]
print(s)

# Task 14: Replace all vowels with '*'
def replace_vowels_with_star(text):
    return ''.join('*' if c.lower() in 'aeiou' else c for c in text)

# Task 15: Replace all occurrences of 'a' with '@'
def replace_a_with_at(text):
    return text.replace('a', '@')

# Task 16: Delete a string and catch error
s = "delete me"
del s
# print(s)  # Will raise NameError

# Task 17: Concatenate strings with +
a = "Hello "
b = "World"
print(a + b)

# Task 18: Append fixed phrase to name
name = "Alice"
print(name + ", Welcome!")

# Task 19: Combine user input with phrase
input_text = input("Enter something: ")
print("You entered: " + input_text + " - Thanks!")

# Task 20: Repeat word using * operator
print("Hello" * 5)


# Task 21: Use len() to count characters
print(len("Python"))

# Task 22: Convert to lowercase
print("PYTHON".lower())

# Task 23: Convert to uppercase
print("python".upper())

# Task 24: Remove leading/trailing whitespace
print("   space   ".strip())

# Task 25: Replace 'bad' with 'good'
print("This is bad".replace("bad", "good"))

# Task 26: Split comma-separated string
csv = "apple,banana,mango"
print(csv.split(","))

# Task 27: Join list of words with -
print("-".join(["one", "two", "three"]))

# Task 28: Count occurrences of 'a'
print("banana".count("a"))

# Task 29: Find index of 'o' in Google
print("Google".find("o"))

# Task 30: Convert sentence to lowercase, then dash-separated
print("Python is FUN".lower().replace(" ", "-"))

# Task 31: Count vowels and consonants
def count_vowels_consonants(text):
    vowels = sum(1 for c in text.lower() if c in 'aeiou')
    consonants = sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
    return vowels, consonants

# Task 32: Remove all spaces
print("Remove space from me".replace(" ", ""))

# Task 33: Split and print each word on new line
for word in "Split these words now".split():
    print(word)

# Task 34: Print middle character if odd length
s = "middle"
if len(s) % 2 != 0:
    print(s[len(s) // 2])

# Task 35: Return first and last characters combined
def first_last_combined(s):
    return s[0] + s[-1]


# Task 36: Concatenate first and last name
fname = "John"
lname = "Doe"
print(fname + " " + lname)

# Task 37: Ask for name and print 3 times
name = input("Enter your name: ")
print((name + " ") * 3)

# Task 38: Join five words with +
sentence = "" + "Python" + " is" + " awesome" + " for" + " learning"
print(sentence)

# Task 39: Join characters into word using .join()
chars = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(chars))

# Task 40: Print welcome message using input
user = input("Enter your name: ")
print("Welcome " + user)


# Task 41: Use f-string for sentence
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Task 42: Use .format() for summation
print("The sum of {} and {} is {}".format(5, 7, 5+7))

# Task 43: Use % formatting for price
product = "Laptop"
price = 59999.99
print("%s costs ₹%.2f" % (product, price))

# Task 44: Function printing result using all formatting styles
def student_result(name, marks):
    print(f"{name} scored {marks}")
    print("{} scored {}".format(name, marks))
    print("%s scored %d" % (name, marks))

# Task 45: Format table of product and price
products = [("Pen", 10), ("Notebook", 55), ("Bag", 500)]
for name, price in products:
    print(f"{name:<10} | ₹{price:>5}")

# Task 46: User input and .format() output
name = input("Name: ")
age = input("Age: ")
print("{} is {} years old.".format(name, age))

# Task 47: Print temperature in °C and °F using f-string
celsius = 35
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature is {celsius}°C or {fahrenheit}°F")

# Task 48: Print discounted price dynamically
discounted_price = 999
print(f"The discounted price is ₹{discounted_price}")

# Task 49: Function to format employee details
def format_employee(name, role):
    return f"{name} works as a {role}"

# Task 50: Function to print formatted weather report
def weather_report(city, temp):
    print(f"Weather in {city}: {temp}°C")
    print("Weather in {}: {}C".format(city, temp))
    print("Weather in %s: %dC" % (city, temp))