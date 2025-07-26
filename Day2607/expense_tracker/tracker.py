import csv
import os
from datetime import datetime

FILE = "expenses.csv"
BUDGET_LIMIT = 10000  # Example: ₹10,000 monthly budget

def load_expenses():
    expenses = []
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
    return expenses

def add_expense(amount, category):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "amount", "category"])
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow({"date": date, "amount": amount, "category": category})

def total_monthly_expense(expenses):
    current_month = datetime.now().strftime("%Y-%m")
    return sum(e['amount'] for e in expenses if e['date'].startswith(current_month))

def category_summary(expenses):
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
    return summary
