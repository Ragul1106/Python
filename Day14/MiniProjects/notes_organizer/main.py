import os

BASE_DIR = "notes"

def create_category(category):
    path = os.path.join(BASE_DIR, category)
    os.makedirs(path, exist_ok=True)
    return path

def add_note():
    category = input("Enter category (e.g., Work, Personal): ").strip()
    path = create_category(category)

    title = input("Note Title: ").strip()
    content = input("Enter your note content:\n")

    filename = f"{title.replace(' ', '_')}.txt"
    filepath = os.path.join(path, filename)

    with open(filepath, "w") as f:
        f.write(content)

    print(f"✅ Note saved in category '{category}' as '{filename}'.")

def view_notes():
    category = input("Enter category to view: ").strip()
    path = os.path.join(BASE_DIR, category)

    if not os.path.exists(path):
        print("❌ Category not found.")
        return

    files = os.listdir(path)
    if not files:
        print("📂 No notes in this category.")
        return

    for file in files:
        print(f"\n📄 {file}")
        with open(os.path.join(path, file), "r") as f:
            print(f.read())

def search_note():
    keyword = input("Enter keyword to search: ").lower()
    if not os.path.exists(BASE_DIR):
        print("❌ No notes found.")
        return

    found = False
    for category in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, category)
        for file in os.listdir(path):
            with open(os.path.join(path, file), "r") as f:
                content = f.read()
                if keyword in content.lower() or keyword in file.lower():
                    print(f"\n🔍 Found in {category}/{file}")
                    print(content)
                    found = True
    if not found:
        print("❌ No match found.")

def main():
    while True:
        print("\n==== Notes Organizer ====")
        print("1. Add Note")
        print("2. View Notes by Category")
        print("3. Search Notes")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_note()
        elif choice == "4":
            print("👋 Exiting Notes Organizer.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
