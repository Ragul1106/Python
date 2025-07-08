students = []
count = 0

while count < 10:
    name = input(f"Enter student {count+1} name (or press Enter to skip): ")
    if not name:
        continue
    students.append(name)
    count += 1
else:
    print("\nAttendance completed!")
    print("Present students:", students)