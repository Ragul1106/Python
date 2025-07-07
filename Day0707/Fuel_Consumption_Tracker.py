consumption = [float(input(f"Enter day {i+1} consumption (liters): ")) for i in range(7)]

total = sum(consumption)
if total > 50:
    print(f"Alert! High fuel consumption: {total} liters this week")