balance = 10000

for _ in range(3):
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        balance += amount
    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
    elif choice == 3:
        print(f"Current Balance: ₹{balance:.2f}")