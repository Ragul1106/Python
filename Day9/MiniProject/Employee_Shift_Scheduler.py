shifts = [
    (101, "Ragul", ("09:00", "17:00")),
    (102, "Ranjith", ("13:00", "21:00")),
    (103, "Heera", ("07:00", "15:00"))
]

print("Early shift employees:")
for emp_id, name, (start, end) in shifts:
    if start < "12:00":
        print(f"{name}: {start}-{end}")


print("\nShift hours:")
for _, name, (start, end) in shifts:
    hours = int(end[:2]) - int(start[:2])
    print(f"{name}: {hours} hours")