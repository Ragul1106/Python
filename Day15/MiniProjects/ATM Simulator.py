class InsufficientFundsError(Exception):
    pass

class ATM:
    def __init__(self, balance=1000):
        self.balance = balance
    
    def withdraw(self, amount):
        try:
            assert amount > 0, "Amount must be positive"
            if amount > self.balance:
                raise InsufficientFundsError("Not enough funds")
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        except AssertionError as e:
            print(f"Error: {e}")
        except InsufficientFundsError as e:
            print(f"Error: {e}")
    
    def deposit(self, amount):
        try:
            assert amount > 0, "Amount must be positive"
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        except AssertionError as e:
            print(f"Error: {e}")

atm = ATM()
atm.withdraw(500)
atm.withdraw(600)  
atm.deposit(-100)  