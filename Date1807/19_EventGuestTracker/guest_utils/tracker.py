event_data = {}

def add_guest(event_id, guest_name, rsvp_status):
    event_key = (event_id.strip(),)
    
    if event_key not in event_data:
        event_data[event_key] = {
            "guests": set(),
            "rsvp": {}
        }

    guests = event_data[event_key]["guests"]
    rsvp = event_data[event_key]["rsvp"]

    if guest_name in guests:
        print(f"Guest '{guest_name}' already added for event {event_id}.")
    else:
        guests.add(guest_name)
        rsvp[guest_name] = rsvp_status.strip().capitalize()
        print(f"Guest '{guest_name}' added to event {event_id} with RSVP '{rsvp_status}'.")

def view_guests():
    if not event_data:
        print("No event data available.")
        return

    for event_key, info in event_data.items():
        print(f"\nEvent ID: {event_key[0]}")
        for guest in info["guests"]:
            print(f"- {guest} (RSVP: {info['rsvp'][guest]})")
