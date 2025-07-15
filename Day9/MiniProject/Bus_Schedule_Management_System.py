routes = [
    (101, "08:00", "10:30", ("Stop1", "Stop2", "Stop3")),
    (102, "09:15", "12:45", ("StopA", "StopB", "StopC", "StopD")),
    (103, "14:00", "16:30", ("StopX", "StopY"))
]

def show_schedule():
    for route in routes:
        num, dep, arr, stops = route
        print(f"\nBus #{num}: {dep} to {arr}")
        print(f"Stops: {', '.join(stops)}")

show_schedule()

route_to_update = 102
new_stops = ("StopA", "StopB", "StopE")  
updated_routes = [
    route if route[0] != route_to_update else (route[0], route[1], route[2], new_stops)
    for route in routes
]
print("\nAfter update:")
show_schedule()