class InvalidMarkError(Exception):
    pass

def generate_marksheet(students):
    for student in students:
        try:
            name = student['name']
            marks = student['marks']
            
            for subject, mark in marks.items():
                if mark < 0:
                    raise ValueError("Marks cannot be negative")
                if mark > 100:
                    raise InvalidMarkError("Marks cannot exceed 100")
                    
            total = sum(marks.values())
            average = total / len(marks)
            
        except ValueError as e:
            print(f"Skipping {name}: {e}")
            continue
        except InvalidMarkError as e:
            print(f"Skipping {name}: {e}")
            continue
        else:
            print(f"{name}'s average: {average:.2f}")
        finally:
            print("-" * 30)

students = [
    {'name': 'Alice', 'marks': {'Math': 90, 'Science': 85}},
    {'name': 'Bob', 'marks': {'Math': -5, 'Science': 110}},
    {'name': 'Charlie', 'marks': {'Math': 80, 'Science': 75}}
]

generate_marksheet(students)