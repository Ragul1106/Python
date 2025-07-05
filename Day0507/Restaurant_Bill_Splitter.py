items = [float(x) for x in input("Enter item prices (space separated): ").split()]
friends = int(input("Number of friends: "))

total = sum(items)
per_person = total / friends

print(f"\nTotal Bill: ₹{total:.2f}")
print(f"Each pays: ₹{per_person:.2f}")