from api import get_weather
from utils import log_weather, forecast_generator

def main():
    print("🌦️ Welcome to the Weather App 🌦️")
    while True:
        city = input("\nEnter city name (or 'exit'): ").strip()
        if city.lower() == 'exit':
            print("👋 Goodbye!")
            break
        result = get_weather(city)
        if result:
            weather, raw = result
            print(f"\n📍 Weather in {city.title()}:")
            print(weather)

            log_weather(city, weather)

            print("\n📅 3-Day Forecast:")
            for forecast in forecast_generator(city):
                print(forecast)
        else:
            print("⚠️ Could not fetch weather data.")

if __name__ == "__main__":
    main()
