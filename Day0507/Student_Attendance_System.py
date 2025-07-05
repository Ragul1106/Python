students = input("Enter student names separated by comma: ").split(',')
present_count = 0
for student in students:
    status = input(f"Is {student.strip()} present (P/A)? ").upper()
    if status == 'P':
        present_count += 1
print(f"Total Present: {present_count} / {len(students)}")