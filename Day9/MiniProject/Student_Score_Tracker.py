students = [
    ("Ragul", (85, 90, 78)),
    ("Heera", (92, 88, 95)),
    ("Libi", (78, 85, 80))
]

def show_student_scores():
    for student in students:
        name, scores = student  
        avg = sum(scores) / len(scores)
        print(f"{name}: Math={scores[0]}, Physics={scores[1]}, Chemistry={scores[2]}")
        print(f"  Average: {avg:.1f}\n")

print("Heera's Physics score:", students[1][1][1])  
show_student_scores()