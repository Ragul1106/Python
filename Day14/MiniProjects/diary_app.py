import os
from datetime import datetime

DIARY_DIR = "diary_entries"

def create_diary_dir():
    if not os.path.exists(DIARY_DIR):
        os.makedirs(DIARY_DIR)

def get_filename():
    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(DIARY_DIR, f"{today}.txt")

def write_entry():
    create_diary_dir()
    print("\n📝 Write your diary entry. Type 'END' on a new line to finish.\n")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    with open(get_filename(), "a") as f:
        f.write("\n".join(lines) + "\n")
    print("✅ Entry saved.")

def view_entry(date_str):
    filename = os.path.join(DIARY_DIR, f"{date_str}.txt")
    if not os.path.exists(filename):
        print("❌ No entry found for that date.")
        return
    with open(filename, "r") as f:
        print("\n📖 Diary Entry:")
        print(f.read())

def main():
    while True:
        print("\n==== Simple Diary App ====")
        print("1. Write today's entry")
        print("2. View previous entry")
        print("3. Exit")
        choice = input("Select option: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            date_input = input("Enter date (YYYY-MM-DD): ")
            view_entry(date_input)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
