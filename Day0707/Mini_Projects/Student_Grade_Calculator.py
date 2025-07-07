name = input("Enter student name: ")
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]

average = sum(marks) / len(marks)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
else:
    grade = 'D'

print(f"\n{name}'s Grade Report:")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")