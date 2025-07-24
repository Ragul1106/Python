def get_valid_grade(prompt):
    try:
        grade = float(input(prompt))
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        return grade
    except ValueError as e:
        print(f"Invalid input: {e}")
        return get_valid_grade(prompt)  # Recursive call

def grade_calculator():
    grades = []
    try:
        while True:
            grade = get_valid_grade("Enter grade (or 'done' to finish): ")
            grades.append(grade)
    except KeyboardInterrupt:
        pass
    finally:
        if grades:
            average = sum(grades) / len(grades)
            print(f"Average grade: {average:.2f}")
            print(f"Total grades entered: {len(grades)}")
        else:
            print("No grades entered")

grade_calculator()