import csv
from expense import Expense

CSV_FILE = 'data/expenses.csv'

def save_expense(expense):
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["amount", "category", "date"])
        writer.writerow(expense.to_dict())

def load_expenses():
    expenses = []
    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses

def view_by_category(expenses, category):
    return [e for e in expenses if e['category'].lower() == category.lower()]

def view_by_month(expenses, month):
    return [e for e in expenses if e['date'].startswith(month)]

def view_over_amount(expenses, limit):
    return [e for e in expenses if float(e['amount']) > limit]

def unique_categories(expenses):
    return set(e['category'] for e in expenses)
