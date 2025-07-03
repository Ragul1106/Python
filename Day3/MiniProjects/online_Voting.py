user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_citizenship = input("Enter your citizenship: ")

print(f"\nDetails:")
print(f"Name: {(user_name)}")
print(f"Age: {(user_age)}")
print(f"Citizenship: {(user_citizenship)}")

if user_age >= 18 and user_citizenship.lower() == "indian":
    print(f"\nHello {user_name}, you are eligible to vote in India.")
else:
    print(f"\nSorry {user_name}, you are not eligible to vote in India.")
