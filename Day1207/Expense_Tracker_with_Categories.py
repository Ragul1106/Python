expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append({"amount": amount, "category": category})
    print("Expense recorded!")

def show_summary():
    print("\nExpense Summary:")
    total = sum(e["amount"] for e in expenses)
    print(f"Total: ₹{total:.2f}")
    
    categories = {}
    for e in expenses:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]
    
    for cat, amt in categories.items():
        print(f"{cat}: ₹{amt:.2f}")

while True:
    print("\n1. Add Expense\n2. Show Summary\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        show_summary()
    elif choice == '3':
        break
    else:
        print("Invalid choice")