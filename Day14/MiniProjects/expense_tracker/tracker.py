import os
import csv
from datetime import datetime

EXPENSE_DIR = "expenses"
os.makedirs(EXPENSE_DIR, exist_ok=True)

def get_month_filename():
    now = datetime.now()
    return os.path.join(EXPENSE_DIR, f"{now.year}-{now.month:02}.csv")

def add_expense():
    category = input("Enter category (e.g., Food, Travel, Rent): ")
    amount = input("Enter amount: ₹")
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    row = [date, category, amount]
    file = get_month_filename()
    file_exists = os.path.exists(file)

    with open(file, "a", newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Category", "Amount"])
        writer.writerow(row)

    print("✅ Expense recorded.")

def view_summary():
    file = get_month_filename()
    if not os.path.exists(file):
        print("📂 No expense data found for this month.")
        return

    category_totals = {}
    total = 0
    with open(file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["Category"]
            amt = float(row["Amount"])
            category_totals[cat] = category_totals.get(cat, 0) + amt
            total += amt

    print("\n📊 Monthly Summary:")
    for cat, amt in category_totals.items():
        print(f" - {cat}: ₹{amt:.2f}")
    print(f"💸 Total Expenses: ₹{total:.2f}\n")

def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("👋 Exiting Expense Tracker.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
