contacts = {}

def add_contact(**kwargs):
    contacts.update(kwargs)
    return sorted(contacts.items())

def search_contact(name):
    return contacts.get(name, "Contact not found")

add_contact(Alice="123-4567", Bob="987-6543")
print("All contacts:", add_contact(Charlie="555-1234"))
print("Search Alice:", search_contact("Alice"))