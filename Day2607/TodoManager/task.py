from datetime import datetime

class Task:
    def __init__(self, title, priority, due_date, is_completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.is_completed = is_completed

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date,
            "is_completed": self.is_completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["title"],
            data["priority"],
            data["due_date"],
            data["is_completed"]
        )
