from contact_book import ContactBook
from generator import contact_generator

def menu():
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. View All Contacts")
    print("6. Exit")

def main():
    book = ContactBook()

    while True:
        menu()
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                book.add_contact(name, phone, email)

            elif choice == "2":
                name = input("Enter name to delete: ")
                book.delete_contact(name)

            elif choice == "3":
                name = input("Enter name to update: ")
                phone = input("New Phone (or leave blank): ")
                email = input("New Email (or leave blank): ")
                book.update_contact(name, phone if phone else None, email if email else None)

            elif choice == "4":
                name = input("Enter name to search: ")
                contact = book.search_contact(name)
                print(contact if contact else "Not found")

            elif choice == "5":
                print("\nAll Contacts:")
                for contact in contact_generator(book.contacts):
                    print(contact)

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
