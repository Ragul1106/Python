from parcel.tracker import add_parcel, update_status, track_parcel, parcel_data

def main():
    while True:
        print("\n1. Add Parcel\n2. Update Status\n3. Track Parcel\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            pid = input("Enter Tracking ID: ")
            city = input("Enter Origin City: ")
            add_parcel(pid, city)

        elif choice == "2":
            pid = input("Enter Tracking ID: ")
            status = input("Enter Status (e.g., Dispatched, In Transit, Delivered): ")
            city = input("Enter Current City: ")
            update_status(pid, status, city)

        elif choice == "3":
            pid = input("Enter Tracking ID: ")
            track_parcel(pid)

        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()