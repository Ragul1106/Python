from flight.booking import book_flight, show_all_bookings
from flight.payment import process_payment

bookings = {}
destinations = set()

def main():
    while True:
        print("\n1. Book Flight\n2. Show Bookings\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            pid = input("Enter Passenger ID: ")
            name = input("Enter Passenger Name: ")
            dest = input("Enter Destination: ")

            passenger_id = (pid.strip(),)
            if dest in destinations:
                print("Destination already booked by someone else.")
            else:
                fare = float(input("Enter Fare Amount: "))
                paid = process_payment(name, fare)
                if paid:
                    book_flight(bookings, passenger_id, name, dest)
                    destinations.add(dest)

        elif choice == "2":
            show_all_bookings(bookings)

        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
            
