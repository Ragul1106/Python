import json
import os

FILE = "resumes.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_resume():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    skills = input("Skills (comma-separated): ").split(",")
    experience = input("Years of Experience: ")

    resume = {
        "name": name.strip(),
        "email": email.strip(),
        "phone": phone.strip(),
        "skills": [s.strip() for s in skills],
        "experience": experience.strip()
    }

    data = load_data()
    data.append(resume)
    save_data(data)
    print("✅ Resume added.")

def view_resumes():
    data = load_data()
    if not data:
        print("📂 No resumes found.")
        return

    for r in data:
        print(f"\n👤 {r['name']}")
        print(f"📧 Email: {r['email']}")
        print(f"📞 Phone: {r['phone']}")
        print(f"🛠️ Skills: {', '.join(r['skills'])}")
        print(f"🧰 Experience: {r['experience']} years")

def search_by_name():
    name = input("Enter name to search: ").strip().lower()
    data = load_data()
    found = False

    for r in data:
        if r['name'].lower() == name:
            print(f"\n👤 {r['name']}")
            print(f"📧 Email: {r['email']}")
            print(f"📞 Phone: {r['phone']}")
            print(f"🛠️ Skills: {', '.join(r['skills'])}")
            print(f"🧰 Experience: {r['experience']} years")
            found = True
            break
    if not found:
        print("❌ No matching profile found.")

def update_resume():
    name = input("Enter name to update: ").strip().lower()
    data = load_data()
    for r in data:
        if r['name'].lower() == name:
            r['email'] = input("New Email: ").strip()
            r['phone'] = input("New Phone: ").strip()
            r['skills'] = input("New Skills (comma): ").split(",")
            r['experience'] = input("New Experience: ").strip()
            save_data(data)
            print("✅ Resume updated.")
            return
    print("❌ No profile found to update.")

def main():
    while True:
        print("\n==== Resume Collector ====")
        print("1. Add Resume")
        print("2. View All Resumes")
        print("3. Search Resume by Name")
        print("4. Update Resume")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_resume()
        elif choice == "2":
            view_resumes()
        elif choice == "3":
            search_by_name()
        elif choice == "4":
            update_resume()
        elif choice == "5":
            print("👋 Exiting Resume Collector.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
