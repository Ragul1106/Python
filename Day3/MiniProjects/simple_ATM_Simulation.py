initial_balance = float(input("Enter your initial balance: ₹ "))

transaction_amount = float(input("Enter transaction amount: ₹ "))

transaction_type = input("Enter transaction type (deposit/withdraw): ").lower()

if transaction_type == "deposit":
    initial_balance += transaction_amount
    print(f"\nDeposit successful! New balance: ₹ {initial_balance}")
elif transaction_type == "withdraw":
    if transaction_amount <= initial_balance:
        initial_balance -= transaction_amount
        print(f"\nWithdrawal successful! New balance: ₹ {initial_balance}")
    else:
        print(f"\nInsufficient balance! Current balance: ₹ {initial_balance}")
else:
    print("\nInvalid transaction type.")
