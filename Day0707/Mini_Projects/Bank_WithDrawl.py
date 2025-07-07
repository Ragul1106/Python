balance = float(input("Enter your current balance: ₹"))
amount = float(input("Enter withdrawal amount: ₹"))

if amount <= balance:
    balance -= amount
    print(f"Withdrawal successful. New balance: ₹{balance:.2f}")
else:
    print("Insufficient funds!")