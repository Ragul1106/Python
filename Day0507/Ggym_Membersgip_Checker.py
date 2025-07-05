name = input("Enter your name: ")
age = int(input("Enter your age: "))
bmi = float(input("Enter your BMI: "))

if age > 18 and bmi < 25:
    print(f"{name}, you are eligible for gym membership!")
else:
    print(f"{name}, you are not eligible for gym membership.")