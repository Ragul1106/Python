total_withdrawn = 0
MAX_LIMIT = 10000

while total_withdrawn < MAX_LIMIT:
    amount = input("Enter amount to withdraw (or 'stop' to end): ")
    if amount.lower() == 'stop':
        break
    
    amount = float(amount)
    if total_withdrawn + amount > MAX_LIMIT:
        print(f"Cannot withdraw. You can withdraw up to ₹{MAX_LIMIT - total_withdrawn}")
        continue
    
    total_withdrawn += amount
    print(f"Withdrawn: ₹{amount}. Total: ₹{total_withdrawn}")

print(f"Final amount withdrawn: ₹{total_withdrawn}")