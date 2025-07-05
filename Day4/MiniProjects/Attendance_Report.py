students = input("Enter student names separated by comma: ").split(',')
print("\nAttendance Report:")
for roll, name in enumerate(students, start=101):
    print(f"Roll No: {roll}, Name: {name.strip()}, Status: Present")