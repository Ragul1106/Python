attendance = ['Alice', 'Bob', 'Alice']
master_list = ['Alice', 'Bob', 'Charlie']

def take_attendance():
    name = input("Student name: ")
    attendance.append(name)

def show_attendance():
    present = list(set(attendance))
    absent = [s for s in master_list if s not in present]
    print(f"\nPresent ({len(present)}): {', '.join(present)}")
    print(f"Absent ({len(absent)}): {', '.join(absent)}")
take_attendance()
show_attendance()