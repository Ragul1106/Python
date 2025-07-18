def assign_shift(shift_db, emp_id, name, shift):
    if emp_id not in shift_db:
        shift_db[emp_id] = {"name": name, "shifts": set()}
    if shift in shift_db[emp_id]["shifts"]:
        print(f"{name} already assigned to {shift} shift.")
    else:
        shift_db[emp_id]["shifts"].add(shift)
        print(f"Shift '{shift}' assigned to {name}.")

def view_shifts(shift_db):
    if not shift_db:
        print("No shift assignments yet.")
        return
    for emp_id, info in shift_db.items():
        print(f"Employee ID: {emp_id[0]}, Name: {info['name']}, Shifts: {', '.join(info['shifts'])}")
