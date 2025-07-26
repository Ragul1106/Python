from contact import Contact
from manager import load_contacts, save_contacts, search_by_name, search_by_phone, group_by_category, edit_contact
from csv_exporter import export_to_csv

contacts = load_contacts()

def display(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. {c.name} | {c.phone} | {c.email} | {c.category}")

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    category = input("Category (family/work/etc.): ")
    contacts.append(Contact(name, phone, email, category))
    save_contacts(contacts)
    print("Contact added!")

def delete_contact():
    display(contacts)
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        contacts.pop(index)
        save_contacts(contacts)
        print("Deleted.")
    except:
        print("Invalid input.")

def edit_contact_menu():
    display(contacts)
    try:
        index = int(input("Enter contact number to edit: ")) - 1
        contact = contacts[index]
        print("Leave field blank to keep current.")
        name = input(f"New name ({contact.name}): ") or contact.name
        phone = input(f"New phone ({contact.phone}): ") or contact.phone
        email = input(f"New email ({contact.email}): ") or contact.email
        category = input(f"New category ({contact.category}): ") or contact.category
        edit_contact(contact, name, phone, email, category)
        save_contacts(contacts)
        print("Updated.")
    except:
        print("Invalid input.")

def search():
    opt = input("Search by (1) Name or (2) Phone? ")
    if opt == "1":
        name = input("Enter name: ")
        result = search_by_name(contacts, name)
    else:
        phone = input("Enter phone: ")
        result = search_by_phone(contacts, phone)
    display(result)

def show_grouped():
    groups = group_by_category(contacts)
    for category, group in groups.items():
        print(f"\nCategory: {category}")
        display(group)

def main():
    while True:
        print("\n📇 Contact Book")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Group by Category")
        print("7. Export to CSV")
        print("8. Exit")
        choice = input("Select option: ")

        if choice == "1":
            display(contacts)
        elif choice == "2":
            add_contact()
        elif choice == "3":
            edit_contact_menu()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            search()
        elif choice == "6":
            show_grouped()
        elif choice == "7":
            export_to_csv(contacts)
            print("Exported to contacts_export.csv")
        elif choice == "8":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
