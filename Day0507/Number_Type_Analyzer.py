numbers = [int(x) for x in input("Enter numbers (space separated): ").split()]

for num in numbers:
    print(f"\nNumber: {num}")
    print("Even" if num % 2 == 0 else "Odd")
    print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")