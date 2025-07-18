def add_device(device_db, device_id, name, brand):
    if device_id in device_db:
        print("Device already exists.")
        return

    device_db[device_id] = {
        "name": name.strip(),
        "brand": brand.strip()
    }
    print(f"Device '{name}' added.")

def list_devices(device_db):
    if not device_db:
        print("No devices in inventory.")
        return

    for device_id, info in device_db.items():
        print(f"ID: {device_id[0]}, Name: {info['name']}, Brand: {info['brand']}")

def list_brands(device_db):
    brands = set(info["brand"] for info in device_db.values())
    if brands:
        print("Available Brands:", ", ".join(brands))
    else:
        print("No brands added yet.")
