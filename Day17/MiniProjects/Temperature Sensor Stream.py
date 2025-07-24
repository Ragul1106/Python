import random

def temperature_stream():
    temp = 20.0
    while True:
        change = random.uniform(-2, 2)
        temp += change
        override = yield max(0.0, temp)
        if override is not None:
            temp = override

sensor = temperature_stream()
next(sensor)  

for _ in range(20):
    reading = sensor.send(None)  
    print(f"Current temp: {reading:.1f}°C")
    if reading > 100:
        print("CRITICAL TEMPERATURE!")
        break