celsius = input("Enter temperature in Celsius: ")
print(f"Before conversion type: {type(celsius)}")

fahrenheit = (float(celsius) * 9/5) + 32
print(f"\n{celsius}°C is {fahrenheit:.1f}°F")
print(f"After conversion type: {type(fahrenheit)}")