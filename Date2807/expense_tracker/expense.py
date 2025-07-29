from datetime import datetime

class Expense:
    def __init__(self, amount, category, date_str):
        self.amount = float(amount)
        self.category = category
        self.date = datetime.strptime(date_str, "%Y-%m-%d")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%Y-%m-%d")
        }
