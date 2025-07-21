class Movie:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre
    
    def __str__(self):
        return f"{self.title} ({self.genre}, {self.duration} mins)"

class Seat:
    def __init__(self, row, number):
        self.row = row
        self.number = number
        self.is_booked = False
    
    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False
    
    def cancel(self):
        self.is_booked = False
    
    def __str__(self):
        return f"Seat {self.row}{self.number} ({'Booked' if self.is_booked else 'Available'})"

class Ticket:
    def __init__(self, user, movie, seat):
        self.user = user
        self.movie = movie
        self.seat = seat
        self.ticket_id = self.generate_id()
    
    def generate_id(self):
        import random
        return f"TKT{random.randint(1000, 9999)}"
    
    def __str__(self):
        return f"Ticket {self.ticket_id}\nMovie: {self.movie.title}\nSeat: {self.seat.row}{self.seat.number}\nCustomer: {self.user.name}"

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @staticmethod
    def check_seat_availability(seat):
        return not seat.is_booked
    
    def book_ticket(self, movie, seat):
        if self.check_seat_availability(seat):
            if seat.book():
                return Ticket(self, movie, seat)
        return None
    
    def cancel_ticket(self, ticket):
        ticket.seat.cancel()
        return True