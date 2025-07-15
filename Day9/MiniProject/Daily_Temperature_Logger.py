temperatures = [
    ("2023-05-01", (22.5, 28.7)),
    ("2023-05-02", (23.1, 29.3)),
    ("2023-05-03", (21.8, 30.2)),
    ("2023-05-04", (20.5, 27.9))
]

evening_temps = [temp[1][1] for temp in temperatures]
max_evening = max(evening_temps)
print(f"Highest evening temp: {max_evening}°C")

print("\nLast 7 days:")
for date, (morning, evening) in temperatures[-7:]:
    print(f"{date}: {morning}°C (AM), {evening}°C (PM)")