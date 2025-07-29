from expense import Expense
from tracker import save_expense, load_expenses, view_by_category, view_by_month, view_over_amount, unique_categories
from generator import expense_generator
from decorators import validate_input
from utils import is_valid_amount, is_valid_date

@validate_input
def add_expense(amount, category, date):
    if not is_valid_date(date):
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return
    expense = Expense(amount, category, date)
    save_expense(expense)
    print("✅ Expense added successfully.")

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View by Category")
        print("3. View by Month")
        print("4. View Over Amount")
        print("5. View by Date Range")
        print("6. Show Categories")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amt = input("Amount: ")
            cat = input("Category: ")
            dt = input("Date (YYYY-MM-DD): ")
            add_expense(amt, cat, dt)

        elif choice == '2':
            cat = input("Enter category: ")
            exps = view_by_category(load_expenses(), cat)
            for e in exps:
                print(e)

        elif choice == '3':
            month = input("Enter month (YYYY-MM): ")
            exps = view_by_month(load_expenses(), month)
            for e in exps:
                print(e)

        elif choice == '4':
            amt = float(input("Show expenses > amount: "))
            exps = view_over_amount(load_expenses(), amt)
            for e in exps:
                print(e)

        elif choice == '5':
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            gen = expense_generator(load_expenses(), start, end)
            for e in gen:
                print(e)

        elif choice == '6':
            print("Categories:", unique_categories(load_expenses()))

        elif choice == '0':
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
