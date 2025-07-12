transactions = [100, -50, 200]

def add_transaction():
    amount = float(input("Amount (+deposit/-withdrawal): "))
    transactions.append(amount)
    print(f"Added transaction: {amount:.2f}")

def show_balance():
    balance = sum(transactions)
    print(f"\nCurrent Balance: ${balance:.2f}")
    print("Recent Transactions:")
    for t in transactions[-3:]:
        print(f"${t:+.2f}")

# add_transaction()
show_balance()