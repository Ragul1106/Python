temps = [float(x) for x in input("Enter temperatures (space separated): ").split()]

for temp in temps:
    if temp < 20:
        cat = "Cold"
    elif temp <= 30:
        cat = "Warm"
    else:
        cat = "Hot"
    print(f"{temp}°C: {cat}")