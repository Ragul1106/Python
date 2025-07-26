from tracker import load_expenses, add_expense, total_monthly_expense, category_summary, BUDGET_LIMIT
from visualizer import show_pie_chart, show_bar_chart
from exporter import export_to_spreadsheet

def main():
    while True:
        print("\n💸 Expense Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. Category-wise Report")
        print("4. Show Pie Chart")
        print("5. Show Bar Chart")
        print("6. Export to Spreadsheet")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category (e.g., food, travel): ").lower()
                add_expense(amount, category)
                print("Expense added.")
                total = total_monthly_expense(load_expenses())
                print(f"Total this month: ₹{total:.2f}")
                if total > BUDGET_LIMIT:
                    print("⚠️ Budget limit exceeded!")
            except ValueError:
                print("Invalid input.")
        elif choice == "2":
            total = total_monthly_expense(load_expenses())
            print(f"Total expenses this month: ₹{total:.2f}")
        elif choice == "3":
            summary = category_summary(load_expenses())
            for cat, amt in summary.items():
                print(f"{cat.capitalize()}: ₹{amt:.2f}")
        elif choice == "4":
            summary = category_summary(load_expenses())
            show_pie_chart(summary)
        elif choice == "5":
            summary = category_summary(load_expenses())
            show_bar_chart(summary)
        elif choice == "6":
            export_to_spreadsheet()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
