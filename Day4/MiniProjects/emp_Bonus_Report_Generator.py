employees = [("Amit", 95), ("Neha", 82), ("Ravi", 70)]
for name, score in employees:
    if score >= 90:
        bonus = 10000
    elif score >= 75:
        bonus = 5000
    else:
        bonus = 2000
    print(f"Employee: {name}, Score: {score}, Bonus: ₹{bonus}")