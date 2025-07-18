def add_marks(db, student_id, marks_dict):
    subjects = set(marks_dict.keys())
    db[student_id] = {
        "marks": marks_dict,
        "subjects": subjects
    }
    print(f"Marks added for Student {student_id[0]}.")

def calculate_average(db, student_id):
    if student_id not in db:
        print("Student not found.")
        return
    marks = db[student_id]["marks"].values()
    avg = sum(marks) / len(marks)
    print(f"Average Marks for {student_id[0]}: {avg:.2f}")

def display_all(db):
    if not db:
        print("No student data available.")
        return
    for sid, info in db.items():
        print(f"\nStudent ID: {sid[0]}")
        print("Subjects:", ", ".join(info["subjects"]))
        print("Marks:", info["marks"])
