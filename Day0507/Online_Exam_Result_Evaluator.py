marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]

if any(mark < 35 for mark in marks):
    print("Result: Fail")
else:
    total = sum(marks)
    percentage = (total / (len(marks)*100)) * 100
    
    if percentage >= 60:
        division = "First Division"
    elif percentage >= 45:
        division = "Second Division"
    else:
        division = "Third Division"
    
    print(f"Result: Pass ({division})")
    print(f"Percentage: {percentage:.2f}%")