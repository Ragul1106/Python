name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 13:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teen"
elif 20 <= age <= 59:
    category = "Adult"
else:
    category = "Senior"

print(f"\n{name}, you are classified as: {category}")