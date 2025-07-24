from datetime import datetime

class OverBookingError(Exception):
    pass

class InvalidDateError(Exception):
    pass

def hotel_booking():
    total_rooms = 50
    booked_rooms = 35
    
    try:
        check_in = input("Enter check-in date (YYYY-MM-DD): ")
        datetime.strptime(check_in, "%Y-%m-%d")  # Validate date format
        
        guests = int(input("Enter number of guests: "))
        if guests <= 0:
            raise ValueError("Guest count must be positive")
            
        available = total_rooms - booked_rooms
        if guests > available:
            raise OverBookingError(f"Only {available} rooms available")
            
        print("Booking confirmed!")
        
    except ValueError as e:
        print(f"Error: {e}")
    except OverBookingError as e:
        print(f"Error: {e}")
    except Exception:
        print("Error: Invalid date format (use YYYY-MM-DD)")
    finally:
        print("Thank you for using our booking system")

hotel_booking()