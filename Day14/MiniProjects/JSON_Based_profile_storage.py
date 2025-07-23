import json
import os

FILENAME = "profiles.json"

def ensure_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            json.dump({}, f)

def load_profiles():
    ensure_file()
    with open(FILENAME, "r") as f:
        return json.load(f)

def save_profiles(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def add_profile():
    profiles = load_profiles()
    name = input("Name: ")
    email = input("Email: ")
    age = input("Age: ")
    phone = input("Phone: ")

    if name in profiles:
        print("⚠️ Profile with this name already exists.")
        return

    profiles[name] = {
        "email": email,
        "age": age,
        "phone": phone
    }
    save_profiles(profiles)
    print("✅ Profile added.")

def view_profiles():
    profiles = load_profiles()
    if not profiles:
        print("No profiles found.")
        return
    for name, details in profiles.items():
        print(f"\n👤 Name: {name}")
        for key, val in details.items():
            print(f"   {key.title()}: {val}")

def update_profile():
    profiles = load_profiles()
    name = input("Enter name to update: ")
    if name not in profiles:
        print("❌ Profile not found.")
        return

    email = input("New Email: ")
    age = input("New Age: ")
    phone = input("New Phone: ")

    profiles[name] = {
        "email": email,
        "age": age,
        "phone": phone
    }
    save_profiles(profiles)
    print("🔁 Profile updated.")

def delete_profile():
    profiles = load_profiles()
    name = input("Enter name to delete: ")
    try:
        del profiles[name]
        save_profiles(profiles)
        print("🗑️ Profile deleted.")
    except KeyError:
        print("❌ Profile not found.")

if __name__ == "__main__":
    while True:
        print("\n=== JSON Profile Storage App ===")
        print("1. Add Profile")
        print("2. View Profiles")
        print("3. Update Profile")
        print("4. Delete Profile")
        print("5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_profile()
        elif choice == "2":
            view_profiles()
        elif choice == "3":
            update_profile()
        elif choice == "4":
            delete_profile()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice.")
