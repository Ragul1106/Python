visitors = set()
for i in range(5):
    visitors.add(input(f"Enter name of visitor {i+1}: "))

print(f"\nUnique visitors: {len(visitors)}")
print(f"Visitors set: {visitors}")