first = input("Enter your first name: ")
last = input("Enter your last name: ")

email = f"{first.lower()}.{last.lower()}@example.com"
print(f"\nYour email: {email}")
print(f"Email type: {type(email)}")