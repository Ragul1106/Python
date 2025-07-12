expenses = [50.0, 30.5, 75.25]

def add_expense():
    amount = float(input("Expense amount: "))
    expenses.append(amount)
    print(f"Added ${amount:.2f}")

def show_expenses():
    print("\nRecent Expenses:")
    for amount in expenses[-3:]:
        print(f"${amount:.2f}")
    print(f"\nTotal: ${sum(expenses):.2f}")
    
add_expense()
show_expenses()