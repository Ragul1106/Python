events = {}

def register_participant(event, participant):
    events.setdefault(event, {"participants": [], "max": 100})["participants"].append(participant)

def event_full(event):
    return len(events.get(event, {}).get("participants", [])) >= events[event]["max"]

register_participant("Concert", "Ragul")
print("Event full?", event_full("Concert"))