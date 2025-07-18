records = {}

def add_service_record(plate_tuple, owner_name, services):
    if plate_tuple in records:
        records[plate_tuple]["services"].update(services)
        print(f"Updated record for {plate_tuple[0]}")
    else:
        records[plate_tuple] = {
            "owner": owner_name,
            "services": services
        }
        print(f"Added new record for {plate_tuple[0]}")

def view_service_records():
    if not records:
        print("No records found.")
        return

    for plate, info in records.items():
        print(f"\nPlate: {plate[0]}")
        print(f"Owner: {info['owner']}")
        print(f"Services: {', '.join(info['services'])}")
