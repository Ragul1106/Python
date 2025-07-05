marks = float(input("Enter total marks: "))

if marks >= 90:
    grade = "Excellent"
elif marks >= 75:
    grade = "Good"
elif marks >= 50:
    grade = "Average"
else:
    grade = "Poor"

print(f"Grade: {grade}")