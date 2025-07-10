city = "Chennai"
temp = 35
humidity = 60

print("Weather in " + city + ": " + str(temp) + "°C, " + str(humidity) + "% humidity")
print("Weather in {}: {}°C, {}% humidity".format(city, temp, humidity))
print(f"Weather in {city}: {temp}°C, {humidity}% humidity")