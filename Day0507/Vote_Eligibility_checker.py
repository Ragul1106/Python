ages = [int(x) for x in input("Enter ages (space separated): ").split()]

for age in ages:
    print(f"Age {age}: {'Eligible' if age >= 18 else 'Not Eligible'}")