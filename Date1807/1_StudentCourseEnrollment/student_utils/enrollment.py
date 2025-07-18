def enroll_student(student_db, student_id, name):
    if student_id not in student_db:
        student_db[student_id] = {"name": name, "courses": set()}
        print(f"Student '{name}' added.")
    else:
        print(f"Student ID {student_id} already exists.")

def enroll_course(student_db, student_id, course):
    if student_id in student_db:
        student = student_db[student_id]
        if course in student["courses"]:
            print(f"{student['name']} is already enrolled in {course}.")
        else:
            student["courses"].add(course)
            print(f"{course} has been added to {student['name']}'s courses.")
    else:
        print("Student not found.")
