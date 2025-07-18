parcel_data = {}

def add_parcel(tracking_id, origin_city):
    key = (tracking_id.strip(),)
    if key in parcel_data:
        print("Parcel already exists.")
    else:
        parcel_data[key] = {
            "status": "Registered",
            "cities": set([origin_city])
        }
        print(f"Parcel {tracking_id} added from {origin_city}.")

def update_status(tracking_id, status, city):
    key = (tracking_id.strip(),)
    if key not in parcel_data:
        print("Parcel not found.")
    else:
        parcel_data[key]["status"] = status
        parcel_data[key]["cities"].add(city)
        print(f"Status updated: {status} | City added: {city}")

def track_parcel(tracking_id):
    key = (tracking_id.strip(),)
    if key not in parcel_data:
        print("Parcel not found.")
    else:
        data = parcel_data[key]
        print(f"\nTracking ID: {tracking_id}")
        print(f"Status: {data['status']}")
        print("Cities Traveled:", ", ".join(data["cities"]))
