vehicles = [
    ("KA01AB1234", ("2022-01-15", "2022-07-20")),
    ("KA02CD5678", ("2022-03-10", "2022-09-05", "2023-01-12"))
]

def show_service_history(reg_num):
    for vehicle in vehicles:
        num, services = vehicle
        if num == reg_num:
            print(f"\nVehicle {reg_num} service history:")
            for i, date in enumerate(services, 1):
                print(f"Service {i}: {date}")
            return
    print("Vehicle not found")

show_service_history("KA02CD5678")

reg_num = "KA01AB1234"
new_service = "2023-02-18"
updated_vehicles = [
    (num, services + (new_service,)) if num == reg_num else vehicles
    for num, services in vehicles
]

vehicles = updated_vehicles

print("\nAfter adding service:")
show_service_history(reg_num)
