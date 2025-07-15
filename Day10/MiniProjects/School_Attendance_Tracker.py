attendance = {}

def mark_attendance(date, present):
    attendance[date] = present

def student_attendance(name):
    return sum(1 for present in attendance.values() if name in present)

mark_attendance("2023-05-01", ["Ragul", "Bob"])
print("Alice attended", student_attendance("Ranjith"), "days")