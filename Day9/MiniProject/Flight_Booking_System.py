flights = [
    ("F101", "Delhi", "Mumbai", ("Passenger1", "Passenger2", "Passenger3")),
    ("F202", "Bangalore", "Chennai", ("PassengerA", "PassengerB"))
]

def show_flights():
    for flight in flights:
        fid, src, dest, passengers = flight
        print(f"\nFlight {fid}: {src} → {dest}")
        print(f"Passengers ({len(passengers)}):")
        for p in passengers:
            print(f"- {p}")

show_flights()

flight_num = "F202"
new_passenger = "PassengerC"

updated_flights = [
    (fid, src, dest, passengers + (new_passenger,)) if fid == flight_num else (fid, src, dest, passengers)
    for fid, src, dest, passengers in flights
]

flights = updated_flights

print("\nAfter adding passenger:")
show_flights()
