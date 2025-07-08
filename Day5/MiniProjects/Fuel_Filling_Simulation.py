total_fuel = 0
MAX_FUEL = 50

while total_fuel < MAX_FUEL:
    fuel = float(input(f"Current fuel: {total_fuel}L. Add how much? "))
    if fuel <= 0:
        print("Invalid amount")
        continue
    
    if total_fuel + fuel > MAX_FUEL:
        print(f"Can only add {MAX_FUEL - total_fuel}L more")
        continue
    
    total_fuel += fuel

print(f"Tank full! Total fuel: {total_fuel}L")