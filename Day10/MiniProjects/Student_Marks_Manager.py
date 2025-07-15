students = {}

def add_student(name):
    students.setdefault(name, {})

def add_subject(name, subject, mark=0):
    students[name][subject] = mark

def update_mark(name, subject, mark):
    if name in students and subject in students[name]:
        students[name][subject] = mark
    else:
        print("Student/subject not found")

def remove_student(name):
    students.pop(name, None)

def remove_subject(name, subject):
    students.get(name, {}).pop(subject, None)

def list_students():
    for name, subjects in students.items():
        avg = sum(subjects.values()) / len(subjects) if subjects else 0
        print(f"{name}: {subjects} (Avg: {avg:.1f})")

def find_topper():
    return max(students.items(), 
              key=lambda x: sum(x[1].values()))[0]

def passed_students():
    return {name: avg for name, subjects in students.items() 
            if (avg := sum(subjects.values())/len(subjects)) > 50}

add_student("Ragul")
add_subject("Ranjith", "Math", 85)
add_subject("Ragul", "Science", 90)
print("Topper:", find_topper())
print("Passed students:", passed_students())