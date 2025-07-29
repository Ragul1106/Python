import json
from functools import wraps
from datetime import datetime
import os

# Decorator to log each transaction to a file
def audit(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        with open('audit_log.txt', 'a') as f:
            f.write(f"{datetime.now()} - {func.__name__.capitalize()} - Args: {args}, Balance: {self.balance}\n")
        return result
    return wrapper

# Generator to yield transactions by type
def filter_transactions(transactions, txn_type):
    for txn in transactions:
        if txn['type'] == txn_type:
            yield txn

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.transactions = []
        self.filename = f"{self.name}_account.json"
        self.load_account()

    def save_account(self):
        with open(self.filename, 'w') as f:
            json.dump({
                "balance": self.balance,
                "transactions": self.transactions
            }, f, indent=2)

    def load_account(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.balance = data["balance"]
                self.transactions = data["transactions"]

    @audit
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({
            "type": "deposit",
            "amount": amount,
            "time": str(datetime.now())
        })
        self.save_account()

    @audit
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance!")
        self.balance -= amount
        self.transactions.append({
            "type": "withdraw",
            "amount": amount,
            "time": str(datetime.now())
        })
        self.save_account()

    @audit
    def transfer(self, amount, receiver):
        if amount > self.balance:
            raise ValueError("Insufficient balance!")
        self.withdraw(amount)
        receiver.deposit(amount)
        self.transactions.append({
            "type": "transfer",
            "amount": amount,
            "to": receiver.name,
            "time": str(datetime.now())
        })
        self.save_account()

    def apply_interest(self):
        if self.balance > 1000:
            interest = self.balance * 0.02
            self.deposit(interest)
            print(f"Interest of ${interest:.2f} applied.")

    def display_transactions(self):
        print("\nTransaction History:")
        for txn in self.transactions:
            print(f"{txn['time']} - {txn['type'].capitalize()} - ${txn['amount']}")

# -------------------- CLI --------------------

def main():
    print("Welcome to the Bank Account Simulator")
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Show Transactions\n5. Apply Interest\n6. Filter Transactions\n7. Exit")
        choice = input("Choose an option: ")

        try:
            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

            elif choice == '3':
                receiver_name = input("Enter receiver name: ")
                receiver = BankAccount(receiver_name)
                amount = float(input("Enter transfer amount: "))
                account.transfer(amount, receiver)

            elif choice == '4':
                account.display_transactions()

            elif choice == '5':
                account.apply_interest()

            elif choice == '6':
                txn_type = input("Enter transaction type (deposit/withdraw/transfer): ").lower()
                print(f"\nFiltered Transactions ({txn_type}):")
                for txn in filter_transactions(account.transactions, txn_type):
                    print(f"{txn['time']} - {txn['type'].capitalize()} - ${txn['amount']}")

            elif choice == '7':
                print("Goodbye!")
                break

            else:
                print("Invalid option.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
