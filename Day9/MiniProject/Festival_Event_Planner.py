events = [
    ("Concert", ("19:00", "22:00", "Main Stage")),
    ("Workshop", ("11:00", "13:00", "Room A")),
    ("Fireworks", ("21:30", "22:00", "Lake View"))
]

print("Festival Schedule:")
for i, (name, (start, end, location)) in enumerate(events, 1):
    print(f"{i}. {name}: {start}-{end} at {location}")

print("\nEvening events (after 18:00):")
for name, (start, _, _) in events:
    if start >= "18:00":
        print(name)