student = {}
student['name'] = input("Enter student name: ")
student['scores'] = [
    float(input("Enter score for subject 1: ")),
    float(input("Enter score for subject 2: ")),
    float(input("Enter score for subject 3: "))
]

average = sum(student['scores']) / len(student['scores'])
print(f"\n{student['name']}'s average score is {average:.2f}")
print(f"Average is type: {type(average)}")