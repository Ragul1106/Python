name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 13:
    group = "Child"
elif 13 <= age <= 19:
    group = "Teenager"
elif 20 <= age <= 59:
    group = "Adult"
else:
    group = "Senior"

print(f"\n{name}, you are classified as: {group}")