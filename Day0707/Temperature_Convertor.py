celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

if celsius < 20:
    category = "Cold"
elif 20 <= celsius <= 30:
    category = "Warm"
else:
    category = "Hot"

print(f"\n{celsius}°C = {fahrenheit:.1f}°F")
print(f"Condition: {category}")