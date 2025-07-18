from service_manager.services import add_service_record, view_service_records

def main():
    while True:
        print("\n1. Add Service Record\n2. View All Records\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            plate = input("Enter Vehicle Plate Number: ").strip().upper()
            owner = input("Enter Owner Name: ").strip()
            services = input("Enter Services (comma-separated): ").strip().lower().split(',')

            service_set = set([s.strip() for s in services])
            add_service_record((plate,), owner, service_set)

        elif choice == "2":
            view_service_records()

        elif choice == "3":
            break
        else:
            print("Invalid option. Try again.")
if __name__ == "__main__":
    main()
