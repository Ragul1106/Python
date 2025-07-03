age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))

if age < 21:
    print("Not eligible - too young")
elif income < 20000:
    print("Not eligible - income too low")
else:
    print("Congratulations! You are eligible for a loan")