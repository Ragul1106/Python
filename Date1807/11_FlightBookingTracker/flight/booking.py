def book_flight(db, pid, name, destination):
    db[pid] = {
        "name": name,
        "destination": destination
    }
    print(f"Booking confirmed for {name} to {destination}.")

def show_all_bookings(db):
    if not db:
        print("No bookings found.")
        return
    for pid, details in db.items():
        print(f"\nPassenger ID: {pid[0]}")
        print(f"Name: {details['name']}")
        print(f"Destination: {details['destination']}")
