attendance = input("Enter attendance for 7 days (P/A without spaces): ").upper()

present = attendance.count('P')
if present >= 5:
    print(f"Eligible for exam ({present}/7 days present)")
else:
    print(f"Not eligible ({7-present} absences)")