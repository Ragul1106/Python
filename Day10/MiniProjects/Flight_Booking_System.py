flights = {}

def add_passenger(flight_id, passenger):
    flights.setdefault(flight_id, {"passengers": []})["passengers"].append(passenger)

def flight_full(flight_id, max_seats=100):
    return len(flights.get(flight_id, {}).get("passengers", [])) >= max_seats

add_passenger("F101", "Ragul")
print("Flight full?", flight_full("F101"))