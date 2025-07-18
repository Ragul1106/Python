from bus_system.reservation import add_bus, book_seat, view_bookings, buses

def main():
    while True:
        print("\n1. Add Bus\n2. Book Seat\n3. View Bookings\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            bus_id = input("Enter Bus ID: ")
            route = input("Enter Route (From-To): ")
            add_bus(bus_id, route)

        elif choice == "2":
            bus_id = input("Enter Bus ID: ")
            passenger_name = input("Enter Passenger Name: ")
            seat = int(input("Enter Seat Number: "))
            book_seat(bus_id, passenger_name, seat)

        elif choice == "3":
            view_bookings()

        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")
if __name__ == "__main__":
    main()
