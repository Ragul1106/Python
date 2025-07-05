expenses = [float(input(f"Enter day {i+1} expense: ")) for i in range(7)]
total = sum(expenses)

print(f"\nWeekly Total: ₹{total:.2f}")
if total > 3000:
    print("Warning: Cut down on expenses!")