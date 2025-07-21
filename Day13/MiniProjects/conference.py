class Attendee:
    def __init__(self, name, email, company):
        self.name = name
        self.email = email
        self.company = company
        self.sessions = []
    
    def register_for_session(self, session):
        if session.add_attendee(self):
            self.sessions.append(session)
            return True
        return False
    
    def __str__(self):
        return f"{self.name} ({self.company})"

class Event:
    total_attendees = 0
    
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.sessions = []
    
    @classmethod
    def update_attendee_count(cls):
        cls.total_attendees += 1
    
    def add_session(self, session):
        self.sessions.append(session)
    
    def __str__(self):
        return f"{self.name} on {self.date} at {self.location}"

class Session:
    def __init__(self, title, speaker, capacity, event):
        self.title = title
        self.speaker = speaker
        self.capacity = capacity
        self.event = event
        self.attendees = []
        event.add_session(self)
    
    def add_attendee(self, attendee):
        if len(self.attendees) < self.capacity:
            self.attendees.append(attendee)
            Event.update_attendee_count()
            return True
        return False
    
    def __str__(self):
        return f"{self.title} by {self.speaker} ({len(self.attendees)}/{self.capacity})"

class Registration:
    def __init__(self, attendee, event):
        self.attendee = attendee
        self.event = event
        self.registration_id = f"REG-{attendee.email[:3]}-{event.name[:3]}".upper()
    
    def __str__(self):
        return f"Registration {self.registration_id} for {self.event.name}"