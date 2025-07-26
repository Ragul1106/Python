class Contact:
    def __init__(self, name, phone, email, category):
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "category": self.category
        }

    @staticmethod
    def from_dict(data):
        return Contact(data["name"], data["phone"], data["email"], data["category"])
