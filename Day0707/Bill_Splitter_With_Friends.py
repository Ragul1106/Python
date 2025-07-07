total = float(input("Enter total bill amount: ₹"))
friends = int(input("Enter number of friends: "))

if friends >= 1:
    per_person = total / friends
    print(f"Each person pays: ₹{per_person:.2f}")
else:
    print("Invalid number of friends!")