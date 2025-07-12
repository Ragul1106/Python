balance = 10000
transactions = []
attempts = 3
pin = "1234"

def login():
    global attempts
    while attempts > 0:
        entered_pin = input("Enter PIN: ")
        if entered_pin == pin:
            return True
        attempts -= 1
        print(f"Wrong PIN. {attempts} attempts left.")
    return False

def show_menu():
    print("\n1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

def atm():
    if not login():
        print("Account locked. Contact bank.")
        return
    
    while True:
        show_menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            print(f"Balance: ₹{balance:.2f}")
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            balance += amount
            transactions.append(f"Deposit: +₹{amount:.2f}")
            print("Deposit successful!")
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            if amount > balance:
                print("Insufficient funds")
            else:
                balance -= amount
                transactions.append(f"Withdrawal: -₹{amount:.2f}")
                print("Withdrawal successful!")
        elif choice == '4':
            print("\nTransaction History:")
            for t in transactions[-5:]:
                print(t)
        elif choice == '5':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice")

atm()