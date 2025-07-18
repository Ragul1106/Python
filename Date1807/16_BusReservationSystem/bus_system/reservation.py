buses = {}

def add_bus(bus_id, route):
    bus_key = (bus_id.strip(),)
    if bus_key in buses:
        print("Bus already exists.")
    else:
        buses[bus_key] = {
            "route": route,
            "seats": {},
            "booked": set()
        }
        print(f"Bus {bus_id} added on route {route}.")

def book_seat(bus_id, passenger_name, seat_no):
    bus_key = (bus_id.strip(),)
    if bus_key not in buses:
        print("Bus not found.")
        return

    if seat_no in buses[bus_key]["booked"]:
        print("Seat already booked.")
    else:
        buses[bus_key]["seats"][seat_no] = passenger_name
        buses[bus_key]["booked"].add(seat_no)
        print(f"Seat {seat_no} booked for {passenger_name} on Bus {bus_id}.")

def view_bookings():
    if not buses:
        print("No buses available.")
        return

    for bus_key, info in buses.items():
        print(f"\nBus: {bus_key[0]} | Route: {info['route']}")
        if not info["seats"]:
            print("  No bookings yet.")
        else:
            for seat, name in info["seats"].items():
                print(f"  Seat {seat}: {name}")
