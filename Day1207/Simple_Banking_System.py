balance = 5000
transactions = []

def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    balance += amount
    transactions.append(f"Deposit: +₹{amount:.2f}")
    print("Deposit successful!")

def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        transactions.append(f"Withdrawal: -₹{amount:.2f}")
        print("Withdrawal successful!")

def show_history():
    print("\nTransaction History:")
    for t in transactions[-5:]:
        print(t)
    print(f"Current Balance: ₹{balance:.2f}")

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Transaction History\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        deposit()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        show_history()
    elif choice == '4':
        break
    else:
        print("Invalid choice")