numbers = [int(x) for x in input("Enter 10 numbers (space separated): ").split()]

for num in numbers[:10]:  
    print(f"{num} is {'even' if num % 2 == 0 else 'odd'}")