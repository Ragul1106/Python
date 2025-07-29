import json
from functools import wraps
from typing import List, Dict, Set, Generator

class Passenger:
    def __init__(self, name: str, passport: str):
        self.name = name
        self.passport = passport
    
    def __str__(self):
        return f"{self.name} (Passport: {self.passport})"

class Flight:
    def __init__(self, flight_number: str, destination: str, total_seats: int = 60):
        self.flight_number = flight_number
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = self.generate_seats(total_seats)
        self.booked_seats: Set[str] = set()
        self.passenger_manifest: Dict[str, Passenger] = {}  
    
    @staticmethod
    def generate_seats(total_seats: int) -> List[str]:
        """Generate seat numbers (e.g., A1, A2, ..., B1, B2, ...)"""
        rows = total_seats // 6  
        seats = []
        for row in range(1, rows + 1):
            for col in ['A', 'B', 'C', 'D', 'E', 'F']:
                seats.append(f"{col}{row}")
        return seats[:total_seats]  
    
    def get_available_seats(self) -> Generator[str, None, None]:
        """Generator: Yield available seats one by one"""
        for seat in self.available_seats:
            if seat not in self.booked_seats:
                yield seat
    
    def display_status(self) -> None:
        """Display flight status with seat availability"""
        print(f"\nFlight {self.flight_number} to {self.destination}")
        print(f"Seats available: {len(self.available_seats) - len(self.booked_seats)}/{self.total_seats}")
        
        # Display seat map
        print("\nSeat Map (X = booked, O = available):")
        rows = self.total_seats // 6
        for row in range(1, rows + 1):
            row_display = []
            for col in ['A', 'B', 'C', 'D', 'E', 'F']:
                seat = f"{col}{row}"
                if seat in self.booked_seats:
                    row_display.append("X")
                else:
                    row_display.append("O")
            print(f"Row {row}: {' '.join(row_display)}")
    
    def is_seat_available(self, seat: str) -> bool:
        """Check if a seat is available"""
        return seat in self.available_seats and seat not in self.booked_seats
    
    @confirm_booking
    def book_seat(self, seat: str, passenger: Passenger) -> bool:
        """Book a seat for a passenger"""
        try:
            if not self.is_seat_available(seat):
                raise ValueError(f"Seat {seat} is already booked or invalid")
            
            self.booked_seats.add(seat)
            self.passenger_manifest[seat] = passenger
            return True
        except ValueError as e:
            print(f"Booking error: {e}")
            return False
    
    def cancel_booking(self, seat: str) -> bool:
        """Cancel a booking and free up the seat"""
        if seat not in self.booked_seats:
            print(f"No booking found for seat {seat}")
            return False
        
        del self.passenger_manifest[seat]
        self.booked_seats.remove(seat)
        print(f"Booking canceled for seat {seat}")
        return True
    
    def save_bookings(self, filename: str) -> None:
        """Save current bookings to JSON file"""
        bookings_data = {
            "flight_number": self.flight_number,
            "destination": self.destination,
            "bookings": [
                {
                    "seat": seat,
                    "passenger": {
                        "name": passenger.name,
                        "passport": passenger.passport
                    }
                }
                for seat, passenger in self.passenger_manifest.items()
            ]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(bookings_data, f, indent=4)
            print(f"Bookings saved to {filename}")
        except IOError as e:
            print(f"Error saving bookings: {e}")
    
    @classmethod
    def load_bookings(cls, filename: str):
        """Load bookings from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            flight = cls(data["flight_number"], data["destination"])
            for booking in data["bookings"]:
                passenger = Passenger(
                    booking["passenger"]["name"],
                    booking["passenger"]["passport"]
                )
                flight.book_seat(booking["seat"], passenger)
            
            print(f"Bookings loaded from {filename}")
            return flight
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading bookings: {e}")
            return None

def confirm_booking(func):
    """Decorator: Require confirmation before finalizing booking"""
    @wraps(func)
    def wrapper(self, seat: str, passenger: Passenger, *args, **kwargs):
        print(f"\nBooking Summary:")
        print(f"Flight: {self.flight_number} to {self.destination}")
        print(f"Seat: {seat}")
        print(f"Passenger: {passenger}")
        print(f"Price: ${calculate_price(seat):.2f}")
        
        confirm = input("Confirm booking? (y/n): ").lower()
        if confirm == 'y':
            return func(self, seat, passenger, *args, **kwargs)
        else:
            print("Booking canceled by user")
            return False
    return wrapper

def calculate_price(seat: str) -> float:
    """Calculate ticket price based on seat location"""
    if int(seat[1:]) <= 2:
        return 500.00
    elif int(seat[1:]) == 10:
        return 400.00
    elif seat[0] in ['A', 'F']:
        return 300.00
    elif seat[0] in ['C', 'D']:
        return 275.00
    else:
        return 250.00

def main():
    flight = None
    print("Flight Booking System")
    
    while True:
        print("\nMain Menu:")
        print("1. Create New Flight")
        print("2. Load Existing Flight")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            flight_number = input("Enter flight number: ")
            destination = input("Enter destination: ")
            flight = Flight(flight_number, destination)
            print(f"New flight {flight_number} to {destination} created")
            break
        elif choice == "2":
            filename = input("Enter bookings filename: ")
            flight = Flight.load_bookings(filename)
            if flight:
                break
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")
    
    while flight:
        print("\nFlight Booking Menu:")
        print("1. View Flight Status")
        print("2. Book a Seat")
        print("3. Cancel Booking")
        print("4. List Available Seats")
        print("5. Save Bookings")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            flight.display_status()
        elif choice == "2":
            print("\nAvailable seats:")
            available = list(flight.get_available_seats())
            for i, seat in enumerate(available[:20], 1):  
                print(f"{seat}", end=" ")
                if i % 10 == 0:
                    print()
            print("...") if len(available) > 20 else print()

            name = input("Enter passenger name: ")
            passport = input("Enter passport number: ")
            passenger = Passenger(name, passport)

            seat = input("Enter seat number (e.g., A1): ").upper()
            flight.book_seat(seat, passenger)
        elif choice == "3":
            seat = input("Enter seat number to cancel: ").upper()
            flight.cancel_booking(seat)
        elif choice == "4":
            print("\nAvailable seats:")
            for i, seat in enumerate(flight.get_available_seats(), 1):
                print(seat, end=" ")
                if i % 10 == 0:
                    print()
            print()
        elif choice == "5":
            filename = input("Enter filename to save: ")
            flight.save_bookings(filename)
        elif choice == "6":
            save = input("Save bookings before exiting? (y/n): ").lower()
            if save == 'y':
                filename = input("Enter filename: ")
                flight.save_bookings(filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()