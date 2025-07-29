class Weather:
    def __init__(self, temp, humidity, description):
        self.temp = temp
        self.humidity = humidity
        self.description = description

    def __str__(self):
        return f"🌡️ Temp: {self.temp}°C | 💧 Humidity: {self.humidity}% | 🌥️ {self.description}"
