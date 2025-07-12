students = []

def add_student():
    name = input("Enter student name: ")
    marks = []
    for i in range(1, 4):
        marks.append(float(input(f"Enter mark for subject {i}: ")))
    
    avg = sum(marks)/len(marks)
    grade = 'A' if avg >= 90 else 'B' if avg >= 80 else 'C' if avg >= 70 else 'D' if avg >= 60 else 'F'
    
    students.append({
        "name": name,
        "marks": marks,
        "average": avg,
        "grade": grade
    })
    print("Student added!")

def show_results():
    print("\nStudent Results:")
    for s in students:
        print(f"{s['name']}: Avg={s['average']:.2f}, Grade={s['grade']}")

while True:
    print("\n1. Add Student\n2. Show Results\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        show_results()
    elif choice == '3':
        break
    else:
        print("Invalid choice")