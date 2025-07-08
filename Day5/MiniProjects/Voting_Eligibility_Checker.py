eligible = 0
count = 0

while count < 5:
    age = int(input(f"Enter age of person {count+1}: "))
    if age >= 18:
        eligible += 1
        print("Eligible to vote")
    else:
        print("Not eligible")
    count += 1
    pass  

print(f"\nTotal eligible voters: {eligible}")