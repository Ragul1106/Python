# Base Account class
class Account:
    def __init__(self, acc_num, name, initial_balance=0):
        self.acc_num = acc_num
        self.name = name
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.__balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account({self.acc_num}) - {self.name} - ₹{self.__balance}"

# SavingsAccount with limited withdrawal
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > 10000:
            print("Savings account withdrawal limit is ₹10,000")
        else:
            super().withdraw(amount)

# CurrentAccount with higher withdrawal allowance
class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount > 50000:
            print("Current account withdrawal limit is ₹50,000")
        else:
            super().withdraw(amount)

# Transaction class for transfers
class Transaction:
    @staticmethod
    def transfer(sender: Account, receiver: Account, amount: float):
        if amount <= sender.get_balance():
            sender.withdraw(amount)
            receiver.deposit(amount)
            print(f"Transferred ₹{amount} from {sender.name} to {receiver.name}")
        else:
            print("Transfer failed: Insufficient funds.")

"""
# Create accounts
ragul_savings = SavingsAccount("S123", "Ragul", 15000)
kumar_current = CurrentAccount("C456", "Kumar", 60000)

# Deposits
ragul_savings.deposit(3000)

# Withdrawals
ragul_savings.withdraw(12000)  
ragul_savings.withdraw(8000)

# Transfer funds
Transaction.transfer(kumar_current, ragul_savings, 10000)

# Show balances
print(ragul_savings)
print(kumar_current)
"""