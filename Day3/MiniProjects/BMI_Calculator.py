height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Weight category: {category}")
