def print_pattern():
    print("\n1. Star Triangle\n2. Number Pyramid\n3. Square")
    choice = input("Enter pattern type: ")
    
    size = int(input("Enter size: "))
    
    if choice == '1':
        for i in range(1, size+1):
            print('*' * i)
    elif choice == '2':
        for i in range(1, size+1):
            print(' '.join(str(j) for j in range(1, i+1)))
    elif choice == '3':
        for _ in range(size):
            print('*' * size)
    else:
        print("Invalid choice")

print_pattern()