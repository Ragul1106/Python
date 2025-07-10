def get_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'

def calculate_marks():
    marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
    if any(m < 35 for m in marks):
        print("Failed in one or more subjects. Re-evaluation needed.")
        return calculate_marks() 
    avg = sum(marks)/len(marks)
    return avg, get_grade(avg)

average, grade = calculate_marks()
print(f"Average: {average:.2f}, Grade: {grade}")