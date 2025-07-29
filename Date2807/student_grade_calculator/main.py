from student import Student
from grade_utils import (
    calculate_gpa,
    assign_grade,
    find_top_student,
    class_average,
    export_grades_to_csv,
    unique_subjects,
    students_with_grade_A
)

students = {}

def add_student():
    sid = input("Student ID: ")
    name = input("Name: ")
    marks = {}
    subjects = input("Enter subjects (comma separated): ").split(',')

    for sub in subjects:
        sub = sub.strip()
        try:
            score = float(input(f"Marks for {sub}: "))
            if not (0 <= score <= 100):
                raise ValueError
            marks[sub] = score
        except ValueError:
            print("Invalid mark! Must be a number between 0 and 100.")
            return

    students[sid] = Student(sid, name, marks)
    print("✅ Student added.")

def show_all():
    for s in students.values():
        gpa = calculate_gpa(s)
        grade = assign_grade(gpa)
        print(f"{s.student_id}: {s.name} | GPA: {gpa} | Grade: {grade}")

def main():
    while True:
        print("\n--- Student Grade Calculator ---")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Export to CSV")
        print("4. Show Topper")
        print("5. Class Average")
        print("6. Subjects Offered")
        print("7. Students with Grade A")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            show_all()
        elif choice == '3':
            export_grades_to_csv(students)
            print("✅ Exported to grades.csv.")
        elif choice == '4':
            top = find_top_student(students)
            print(f"🏆 Topper: {top.name} (GPA: {calculate_gpa(top)})")
        elif choice == '5':
            print(f"📊 Class Average GPA: {class_average(students)}")
        elif choice == '6':
            print("📚 Subjects:", unique_subjects(students))
        elif choice == '7':
            print("🅰️ Students with Grade A:")
            for s in students_with_grade_A(students):
                print(f"{s.student_id} - {s.name}")
        elif choice == '0':
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
