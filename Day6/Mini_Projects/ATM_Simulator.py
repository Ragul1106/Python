def atm_simulator():
    pin = "1234"
    balance = 10000

    def validate_pin(input_pin):
        return input_pin == pin

    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            print(f"Deposited: ${amount}. New balance: ${balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(amount):
        nonlocal balance
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${balance}")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def change_pin():
        pass  

    while True:
        user_pin = input("Enter your PIN: ")
        if validate_pin(user_pin):
            while True:
                action = input("Choose an action (deposit, withdraw, exit): ").lower()
                if action == "deposit":
                    amount = float(input("Enter deposit amount: "))
                    deposit(amount)
                elif action == "withdraw":
                    amount = float(input("Enter withdrawal amount: "))
                    withdraw(amount)
                elif action == "exit":
                    print(f"Final balance: ${balance}")
                    return
                else:
                    print("Invalid action. Please try again.")
        else:
            print("Invalid PIN. Please try again.")
            
atm_simulator()