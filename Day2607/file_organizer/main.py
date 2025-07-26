import os
from organizer import organize_by_extension
from duplicates import remove_duplicates
from renamer import bulk_rename
from analyzer import find_largest_files
from scheduler import schedule_organize

def main():
    path = input("Enter directory path: ").strip()
    if not os.path.exists(path):
        print("Invalid path.")
        return

    while True:
        print("\n🗃️ File Organizer")
        print("1. Organize by extension")
        print("2. Remove duplicate files")
        print("3. Bulk rename files")
        print("4. Find largest files")
        print("5. Schedule automatic organization")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            organize_by_extension(path)
        elif choice == "2":
            remove_duplicates(path)
        elif choice == "3":
            prefix = input("Enter prefix for renamed files: ")
            bulk_rename(path, prefix)
        elif choice == "4":
            top_n = int(input("Top N largest files to show: "))
            find_largest_files(path, top_n)
        elif choice == "5":
            interval = int(input("Run every how many minutes? "))
            schedule_organize(path, interval)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
