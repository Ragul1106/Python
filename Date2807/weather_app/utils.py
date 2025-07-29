from datetime import datetime

def log_weather(city, weather):
    with open("logs/history.txt", "a") as f:
        f.write(f"{datetime.now()} | {city} | {weather.temp}°C | {weather.humidity}% | {weather.description}\n")

def forecast_generator(city):
    temps = [29, 31, 28]
    descriptions = ["clear sky", "partly cloudy", "light rain"]
    for i in range(3):
        yield f"Day {i+1}: {temps[i]}°C, {descriptions[i].title()}"
