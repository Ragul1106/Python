import json
from contact import Contact

FILE = "contacts.json"

def load_contacts():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return [Contact.from_dict(c) for c in data]
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump([c.to_dict() for c in contacts], f, indent=4)

def search_by_name(contacts, name):
    return [c for c in contacts if name.lower() in c.name.lower()]

def search_by_phone(contacts, phone):
    return [c for c in contacts if phone in c.phone]

def group_by_category(contacts):
    groups = {}
    for c in contacts:
        groups.setdefault(c.category, []).append(c)
    return groups

def edit_contact(contact, name=None, phone=None, email=None, category=None):
    if name: contact.name = name
    if phone: contact.phone = phone
    if email: contact.email = email
    if category: contact.category = category
