def add_record(db, pid, name, age, illness):
    db[pid] = {
        "name": name,
        "age": age,
        "illness": illness
    }
    print(f"Record added for {name} with illness: {illness}")

def view_records(db):
    if not db:
        print("No records found.")
        return
    for pid, info in db.items():
        print(f"\nPatient ID: {pid[0]}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Illness: {info['illness']}")
