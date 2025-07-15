attendance = [
    ("2023-05-01", ("Ragul", "Heera", "Priya")),
    ("2023-05-02", ("Ranjith", "Vetri", "Aishu")),
    ("2023-05-03", ("Libi", "Arul", "Meenu"))
]

student = "Heera"
count = sum(1 for date, students in attendance if student in students)
print(f"{student} attended {count} days")

last_week = attendance[-7:]
print("\nLast week's attendance:")
for date, students in last_week:
    print(f"{date}: {len(students)} students")