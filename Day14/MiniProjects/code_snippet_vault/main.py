import json
import os

DATA_FILE = "snippets.json"

def load_snippets():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_snippets(snippets):
    with open(DATA_FILE, "w") as file:
        json.dump(snippets, file, indent=4)

def add_snippet():
    title = input("Enter snippet title: ")
    description = input("Enter description: ")
    code = input("Paste your code snippet:\n")
    tags = input("Enter tags (comma-separated): ").split(",")

    snippet = {
        "title": title.strip(),
        "description": description.strip(),
        "code": code.strip(),
        "tags": [tag.strip() for tag in tags]
    }

    snippets = load_snippets()
    snippets.append(snippet)
    save_snippets(snippets)
    print("✅ Snippet added successfully!")

def search_snippets():
    keyword = input("Search by title or tag: ").lower()
    snippets = load_snippets()
    found = [s for s in snippets if keyword in s["title"].lower() or keyword in [t.lower() for t in s["tags"]]]
    
    if not found:
        print("❌ No snippets found.")
    else:
        for s in found:
            print("\n🔹 Title:", s["title"])
            print("📝 Description:", s["description"])
            print("🏷️ Tags:", ", ".join(s["tags"]))
            print("📄 Code:\n" + s["code"])
            print("-" * 40)

def main():
    print("== Code Snippet Vault ==")
    while True:
        print("\n1. Add Snippet\n2. Search Snippet\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_snippet()
        elif choice == "2":
            search_snippets()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
