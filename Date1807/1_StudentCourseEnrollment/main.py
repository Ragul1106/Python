from student_utils import enrollment, course_manager

students = {}

def main():
    while True:
        print("\n1. Add Student\n2. Enroll Course\n3. List Courses\n4. Show All Students\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            student_id = (sid,)  
            enrollment.enroll_student(students, student_id, name)

        elif choice == "2":
            sid = input("Enter Student ID: ")
            course = input("Enter Course Name: ")
            student_id = (sid,)
            if course_manager.is_course_available(course):
                enrollment.enroll_course(students, student_id, course)
            else:
                print("Course not available.")

        elif choice == "3":
            course_manager.list_courses()

        elif choice == "4":
            for sid, info in students.items():
                print(f"ID: {sid[0]}, Name: {info['name']}, Courses: {', '.join(info['courses']) if info['courses'] else 'None'}")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
