from datetime import datetime

class NoSeatsAvailableError(Exception):
    pass

class InvalidBookingError(Exception):
    pass

def flight_booking():
    available_seats = 50
    bookings = []
    
    try:
        passenger_id = input("Enter passenger ID: ")
        if not passenger_id.isalnum():
            raise InvalidBookingError("Invalid passenger ID")
            
        flight_date = input("Enter flight date (YYYY-MM-DD): ")
        datetime.strptime(flight_date, "%Y-%m-%d")  # Validate date
        
        seats = int(input("Enter number of seats: "))
        if seats <= 0:
            raise InvalidBookingError("Seats must be positive")
            
        if seats > available_seats:
            raise NoSeatsAvailableError(f"Only {available_seats} seats available")
            
        bookings.append({
            'passenger_id': passenger_id,
            'flight_date': flight_date,
            'seats': seats
        })
        available_seats -= seats
        
        print("Booking confirmed!")
        
    except ValueError:
        print("Error: Invalid date format (use YYYY-MM-DD) or seat number")
    except (InvalidBookingError, NoSeatsAvailableError) as e:
        print(f"Booking error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print(f"Remaining seats: {available_seats}")

flight_booking()