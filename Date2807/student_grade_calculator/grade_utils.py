import csv
from datetime import datetime
from decorators import memoize

@memoize
def calculate_gpa(student):
    total = sum(student.marks.values())
    return round(total / len(student.marks), 2)

def assign_grade(gpa):
    if gpa >= 90:
        return 'A'
    elif gpa >= 80:
        return 'B'
    elif gpa >= 70:
        return 'C'
    elif gpa >= 60:
        return 'D'
    else:
        return 'F'

def find_top_student(students):
    return max(students.values(), key=calculate_gpa)

def class_average(students):
    total_gpa = sum(calculate_gpa(s) for s in students.values())
    return round(total_gpa / len(students), 2)

def export_grades_to_csv(students, filename='grades.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Name', 'GPA', 'Grade'])
        for student in students.values():
            gpa = calculate_gpa(student)
            grade = assign_grade(gpa)
            writer.writerow([student.student_id, student.name, gpa, grade])

def unique_subjects(students):
    return set(subj for student in students.values() for subj in student.marks)

def students_with_grade_A(students):
    for student in students.values():
        gpa = calculate_gpa(student)
        if assign_grade(gpa) == 'A':
            yield student
