age = int(input("Enter age: "))

if age < 13:
    group = "Child"
elif age <= 19:
    group = "Teen"
elif age <= 59:
    group = "Adult"
else:
    group = "Senior"

print(f"Age Group: {group}")