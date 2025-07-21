class Bus:
    def __init__(self, bus_number, capacity, route):
        self.bus_number = bus_number
        self.capacity = capacity
        self.route = route
        self.seats = [Seat(i) for i in range(1, capacity+1)]
    
    def available_seats(self):
        return [seat for seat in self.seats if not seat.is_booked]
    
    def __str__(self):
        return f"Bus {self.bus_number} ({self.route}) - {len(self.available_seats())}/{self.capacity} seats available"

class Passenger:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
    
    def __str__(self):
        return f"Passenger: {self.name} ({self.contact})"

class Seat:
    def __init__(self, number):
        self.number = number
        self.is_booked = False
        self.passenger = None
    
    def book(self, passenger):
        if not self.is_booked:
            self.is_booked = True
            self.passenger = passenger
            return True
        return False
    
    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Seat {self.number}: {status}"

class Booking:
    def __init__(self, bus, seat, passenger):
        self.bus = bus
        self.seat = seat
        self.passenger = passenger
        self.booking_id = f"B{bus.bus_number}-S{seat.number}-{passenger.contact[-4:]}"
    
    def __eq__(self, other):
        return (self.bus.bus_number == other.bus.bus_number and 
                self.seat.number == other.seat.number)
    
    def __str__(self):
        return f"Booking ID: {self.booking_id}\n{self.passenger}\n{self.bus}\nSeat: {self.seat.number}"