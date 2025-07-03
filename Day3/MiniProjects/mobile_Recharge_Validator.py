mobile = input("Enter mobile number: ")
amount = float(input("Enter recharge amount: "))

if len(mobile) == 10 and mobile.isdigit():
    if amount > 10:
        print("Recharge successful!")
    else:
        print("Amount must be greater than ₹10")
else:
    print("Invalid mobile number")