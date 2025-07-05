name = input("Enter student name: ")
class_ = input("Enter class: ")
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
else:
    grade = 'D'

print(f"\nReport Card for {name} (Class {class_})")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")