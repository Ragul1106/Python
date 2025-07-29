from datetime import datetime

class Task:
    def __init__(self, name, deadline, status=False):
        self.name = name
        self.deadline = deadline  
        self.status = status      

    def is_overdue(self):
        return not self.status and datetime.strptime(self.deadline, "%Y-%m-%d").date() < datetime.today().date()

    def to_line(self):
        return f"{self.name}|{self.deadline}|{self.status}\n"

    @staticmethod
    def from_line(line):
        name, deadline, status = line.strip().split("|")
        return Task(name, deadline, status == "True")

    def __str__(self):
        status_str = "✅ Completed" if self.status else ("⚠️ Overdue" if self.is_overdue() else "🕒 Pending")
        return f"{self.name} (Due: {self.deadline}) - {status_str}"
