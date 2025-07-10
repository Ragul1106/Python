def convert_grades(marks):
    grade = lambda m: (
        'A' if m >= 90 else
        'B' if m >= 80 else
        'C' if m >= 70 else
        'D' if m >= 60 else
        'F'
    )
    return list(map(grade, marks))

print(convert_grades([85, 92, 78, 60, 45])) 