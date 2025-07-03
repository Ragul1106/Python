user_name = input("Enter your name: ")
units_consumed = int(input("Enter units consumed: "))

if units_consumed <= 100:
    bill_amount = units_consumed * 2
elif units_consumed <= 300:
    bill_amount = units_consumed * 3
else:
    bill_amount = units_consumed * 5

print(f"\nElectricity Bill for {user_name}: ₹ {bill_amount}")
