import json
import os

CONTACT_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "w") as f:
            json.dump([], f)
    with open(CONTACT_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def create_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added.")

def read_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 No contacts found.")
    for c in contacts:
        print(f"👤 {c['name']} | 📞 {c['phone']} | 📧 {c['email']}")

def update_contact():
    name = input("Enter name to update: ").strip()
    contacts = load_contacts()
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input("New Phone: ").strip()
            c['email'] = input("New Email: ").strip()
            save_contacts(contacts)
            print("🔁 Contact updated.")
            return
    print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    contacts = load_contacts()
    updated = [c for c in contacts if c['name'].lower() != name.lower()]
    if len(updated) < len(contacts):
        save_contacts(updated)
        print("🗑️ Contact deleted.")
    else:
        print("❌ Contact not found.")

def menu():
    while True:
        print("\n==== Contact Manager ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == '1':
            create_contact()
        elif choice == '2':
            read_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("👋 Exiting Contact Manager.")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
