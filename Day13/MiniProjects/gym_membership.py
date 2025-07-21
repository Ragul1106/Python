class Member:
    total_members = 0  
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subscriptions = []
        Member.total_members += 1
    
    def book_slots(self, *sessions):
        for session in sessions:
            self.subscriptions.append(session)
    
    def __str__(self):
        return f"Member: {self.name}, Age: {self.age}, Subscriptions: {len(self.subscriptions)}"

class Trainer:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
    
    def __str__(self):
        return f"Trainer: {self.name}, Specialization: {self.specialization}"

class Schedule:
    def __init__(self, session_name, time, trainer):
        self.session_name = session_name
        self.time = time
        self.trainer = trainer
    
    def __str__(self):
        return f"Session: {self.session_name} at {self.time} with {self.trainer.name}"

class Subscription:
    def __init__(self, member, schedule):
        self.member = member
        self.schedule = schedule
    
    def __str__(self):
        return f"{self.member.name} subscribed to {self.schedule.session_name}"