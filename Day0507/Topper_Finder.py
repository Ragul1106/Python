students = {}
for _ in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

topper = max(students, key=students.get)
print(f"\nTopper: {topper} with {students[topper]} marks")