class Parcel:
    def __init__(self, sender, receiver, weight, dimensions):
        self.sender = sender
        self.receiver = receiver
        self.weight = weight
        self.dimensions = dimensions
        self.tracking = Tracking(self)
        self.status = "Ready for pickup"
    
    @staticmethod
    def validate_dimensions(dimensions):
        return all(d > 0 for d in dimensions)
    
    def __str__(self):
        return f"Parcel ({self.weight}kg, {self.dimensions}) from {self.sender.name} to {self.receiver.name}"

class Sender:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact
    
    def __str__(self):
        return f"Sender: {self.name}"

class Receiver:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact
    
    def __str__(self):
        return f"Receiver: {self.name}"

class Tracking:
    tracking_ids = set()
    
    def __init__(self, parcel):
        self.parcel = parcel
        self.tracking_id = self.generate_tracking_id()
        self.history = []
    
    @classmethod
    def generate_tracking_id(cls):
        import random
        while True:
            new_id = f"TRK{random.randint(100000, 999999)}"
            if new_id not in cls.tracking_ids:
                cls.tracking_ids.add(new_id)
                return new_id
    
    @staticmethod
    def validate_tracking_id(tracking_id):
        return (len(tracking_id) == 9 and 
                tracking_id.startswith('TRK') and 
                tracking_id[3:].isdigit())
    
    def update_status(self, status, location):
        self.history.append((status, location))
        self.parcel.status = status
    
    def get_history(self):
        return self.history
    
    def __str__(self):
        return f"Tracking ID: {self.tracking_id} - Current Status: {self.parcel.status}"