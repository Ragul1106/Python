def sensor_reader():
    return random.randint(80, 100)

print("\nSensor Alert System:")
for reading in iter(lambda: random.randint(80, 100), 99):
    print(f"Current reading: {reading}")
print("ALERT: Critical value reached!")