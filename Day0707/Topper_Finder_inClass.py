students = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}

topper = max(students, key=students.get)
print(f"Topper: {topper} with {students[topper]} marks")