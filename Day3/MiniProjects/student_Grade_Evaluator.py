student_name = input("Enter student's name: ")
marks = int(input("Enter marks obtained: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print(f"\n{student_name} has obtained grade: {grade}")