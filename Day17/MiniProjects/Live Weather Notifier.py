import random

def weather_notifier():
    last_temp = 20
    while True:
        current_temp = last_temp + random.uniform(-3, 3)
        if abs(current_temp - last_temp) >= 5:
            yield f"Significant change: {last_temp:.1f}°C → {current_temp:.1f}°C"
            last_temp = current_temp
        else:
            yield None  
        time.sleep(2)

notifier = weather_notifier()
for _ in range(20):
    update = next(notifier)
    if update:
        print(update)