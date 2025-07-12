students = [['Ram', 85], ['Sam', 78]]

def add_student():
    name = input("Enter student name: ")
    score = int(input("Enter score: "))
    students.append([name, score])

def update_score():
    name = input("Enter student name: ")
    for student in students:
        if student[0] == name:
            student[1] = int(input("Enter new score: "))
            return
    print("Student not found")

def show_scores():
    print("\nStudent Scores:")
    students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
    for student in students_sorted:
        print(f"{student[0]}: {student[1]}")
    print(f"Highest: {students_sorted[0][0]}")
    print(f"Lowest: {students_sorted[-1][0]}")

add_student()
update_score()
show_scores()