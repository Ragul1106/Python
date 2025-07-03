age = int(input("Enter your age: "))
has_aadhar = input("Do you have Aadhar? (yes/no): ").lower()

if age >= 18:
    if has_aadhar == 'yes':
        print("You are eligible for a driving license")
    else:
        print("You need Aadhar to apply")
else:
    print("You must be at least 18 years old")