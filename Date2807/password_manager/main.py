import json
import os
from encryption import encrypt, decrypt
from auth import logged_in, login
from utils import generate_strong_password, weak_passwords

class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def to_dict(self):
        return {"website": self.website, "username": self.username, "password": self.password}

DATA_FILE = "passwords.json"
encryption_key = ""

def load_passwords():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        encrypted_data = f.read()
    if not encrypted_data.strip():
        return []
    decrypted = decrypt(encrypted_data, encryption_key)
    return json.loads(decrypted)

def save_passwords(passwords):
    with open(DATA_FILE, "w") as f:
        encrypted = encrypt(json.dumps(passwords, indent=2), encryption_key)
        f.write(encrypted)

@logged_in
def add_password():
    site = input("Website: ")
    user = input("Username: ")
    pwd = input("Password (leave blank to generate strong one): ")
    if not pwd:
        pwd = generate_strong_password()
        print(f"Generated: {pwd}")
    entry = PasswordEntry(site, user, pwd)
    passwords.append(entry.to_dict())
    save_passwords(passwords)
    print("✅ Password saved!")

@logged_in
def view_passwords():
    if not passwords:
        print("📭 No passwords saved.")
        return
    for p in passwords:
        print(f"{p['website']:15} | {p['username']:10} | {p['password']}")

@logged_in
def delete_password():
    site = input("Enter website to delete: ")
    global passwords
    passwords = [p for p in passwords if p["website"] != site]
    save_passwords(passwords)
    print("🗑️ Deleted.")

@logged_in
def show_weak_passwords():
    print("⚠️ Weak Passwords (<6 chars):")
    for entry in weak_passwords(passwords):
        print(entry)

def menu():
    global encryption_key, passwords
    print("🔐 Welcome to Secure Password Manager")
    encryption_key = input("Enter your encryption key to login: ")
    try:
        passwords = load_passwords()
        login(encryption_key)
    except:
        print("❌ Invalid key or corrupted data.")
        return

    while True:
        print("\n1. Add Password\n2. View All\n3. Delete\n4. Weak Passwords\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            delete_password()
        elif choice == '4':
            show_weak_passwords()
        elif choice == '5':
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    passwords = []
    menu()
