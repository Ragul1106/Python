import logging

logging.basicConfig(filename='attendance.log', level=logging.ERROR)

def track_attendance(students, max_days=30):
    attendance = {}
    
    for student in students:
        try:
            roll_no = student['roll_no']
            days = student['days']
            
            if not isinstance(roll_no, int) or roll_no <= 0:
                raise ValueError(f"Invalid roll number: {roll_no}")
                
            if days < 0 or days > max_days:
                raise ValueError(f"Invalid attendance days: {days}")
                
            attendance[roll_no] = days
            
        except ValueError as e:
            logging.error(f"Error processing {student}: {e}")
            print(f"Skipping invalid record: {e}")
    
    absentees = [roll for roll, days in attendance.items() if days < max_days * 0.75]
    print(f"Absentees (attendance < 75%): {absentees}")

students = [
    {'roll_no': 1, 'days': 28},
    {'roll_no': 2, 'days': 15},
    {'roll_no': -3, 'days': 25},
    {'roll_no': 4, 'days': 35}
]

track_attendance(students)