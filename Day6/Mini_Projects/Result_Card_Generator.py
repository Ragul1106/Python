def generate_result(**subjects):
    marks = list(subjects.values())
    total = sum(marks)
    avg = total / len(marks)

    grade = lambda m: 'A' if m >= 90 else 'B' if m >= 80 else 'C' if m >= 70 else 'D' if m >= 60 else 'F'
    grades = list(map(grade, marks))
    
    status = "Pass" if all(m >= 35 for m in marks) else "Fail"
    
    return total, avg, grades, status

total, avg, grades, status = generate_result(math=85, science=92, english=78)
print(f"Total: {total}, Average: {avg:.2f}, Grades: {grades}, Status: {status}")