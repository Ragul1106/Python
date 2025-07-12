contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added!")

def search_contact():
    term = input("Search name or phone: ")
    found = [c for c in contacts if term.lower() in c["name"].lower() or term in c["phone"]]
    
    if not found:
        print("No contacts found")
        return
    
    print("\nMatching Contacts:")
    for c in found:
        print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Show All\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        print("\nAll Contacts:")
        for c in contacts:
            print(f"Name: {c['name']}, Phone: {c['phone']}")
    elif choice == '4':
        break
    else:
        print("Invalid choice")