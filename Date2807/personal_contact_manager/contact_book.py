import json
import os
from contact import Contact
from utils import is_valid_email, is_valid_phone
from logger import log_action

CONTACTS_FILE = "contacts.json"

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    @log_action
    def add_contact(self, name, phone, email):
        if not is_valid_phone(phone) or not is_valid_email(email):
            raise ValueError("Invalid phone or email format")
        contact = Contact(name, phone, email)
        self.contacts[name] = contact
        self.save_contacts()

    @log_action
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
        else:
            raise KeyError("Contact not found")

    @log_action
    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                if not is_valid_phone(phone):
                    raise ValueError("Invalid phone number")
                self.contacts[name].phone = phone
            if email:
                if not is_valid_email(email):
                    raise ValueError("Invalid email")
                self.contacts[name].email = email
            self.save_contacts()
        else:
            raise KeyError("Contact not found")

    def search_contact(self, name):
        return self.contacts.get(name)

    def save_contacts(self):
        with open(CONTACTS_FILE, "w") as f:
            json.dump({name: c.to_dict() for name, c in self.contacts.items()}, f, indent=4)

    def load_contacts(self):
        if os.path.exists(CONTACTS_FILE):
            with open(CONTACTS_FILE, "r") as f:
                data = json.load(f)
                self.contacts = {name: Contact.from_dict(info) for name, info in data.items()}
