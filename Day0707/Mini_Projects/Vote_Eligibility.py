name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name}, you are eligible to vote!")
else:
    print(f"{name}, you will be eligible in {18-age} years.")