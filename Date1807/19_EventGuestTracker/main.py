from guest_utils.tracker import add_guest, view_guests, event_data

def main():
    while True:
        print("\n1. Add Guest\n2. View Guests\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            event_id = input("Enter Event ID: ")
            name = input("Enter Guest Name: ")
            rsvp = input("RSVP Status (Yes/No): ")

            add_guest(event_id, name, rsvp)

        elif choice == "2":
            view_guests()

        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
