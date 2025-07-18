from inventory_ops.device_ops import add_device, list_devices, list_brands

devices = {}

def main():
    while True:
        print("\n1. Add Device\n2. List Devices\n3. List Brands\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            device_id = input("Enter Device ID: ")
            name = input("Enter Device Name: ")
            brand = input("Enter Brand: ")
            device_key = (device_id.strip(),)
            add_device(devices, device_key, name, brand)

        elif choice == "2":
            list_devices(devices)

        elif choice == "3":
            list_brands(devices)

        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()