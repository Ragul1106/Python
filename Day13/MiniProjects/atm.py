class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.__pin = pin  
        self.__balance = balance  
    
    def verify_pin(self, pin):
        return self.__pin == pin
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def withdraw_multiple(self, *amounts):
        total = sum(amounts)
        return self.withdraw(total)

class ATM:
    @staticmethod
    def display_welcome():
        print("Welcome to the ATM")
    
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account):
        self.accounts[account.account_number] = account
    
    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.verify_pin(pin):
            return account
        return None

class Transaction:
    def __init__(self, account):
        self.account = account
    
    def show_balance(self):
        return self.account.get_balance()
    
    def make_deposit(self, amount):
        return self.account.deposit(amount)
    
    def make_withdrawal(self, amount):
        return self.account.withdraw(amount)
    
    def make_multiple_withdrawals(self, *amounts):
        return self.account.withdraw_multiple(*amounts)