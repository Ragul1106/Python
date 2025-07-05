marks = [float(x) for x in input("Enter marks (space separated): ").split()]

for i, mark in enumerate(marks, 1):
    if mark >= 90:
        grade = 'A'
    elif mark >= 80:
        grade = 'B'
    elif mark >= 70:
        grade = 'C'
    else:
        grade = 'D'
    print(f"Subject {i}: {grade}")