contact = {}
contact['name'] = input("Enter your name: ")
contact['phone'] = input("Enter your phone: ")
contact['email'] = input("Enter your email: ")

print("\nContact Information:")
print(f"Name: {contact['name']}")
print(f"Phone: {contact['phone']}")
print(f"Email: {contact['email']}")

print("\nData Types:")
print(f"Name is type: {type(contact['name'])}")
print(f"Phone is type: {type(contact['phone'])}")
print(f"Email is type: {type(contact['email'])}")