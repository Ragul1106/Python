from weather import get_current_weather, get_forecast, load_favorites, save_favorites

def display_weather(data):
    if data.get("cod") != 200:
        print("❌ Error:", data.get("message", "Unknown error"))
        return
    name = data["name"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"\n📍 {name} — {temp}° — {desc.capitalize()}")

def display_forecast(forecast_data):
    print("\n📅 5-Day Forecast (every 3 hours):")
    for entry in forecast_data["list"][:10]:
        dt_txt = entry["dt_txt"]
        temp = entry["main"]["temp"]
        desc = entry["weather"][0]["description"]
        print(f"{dt_txt} | {temp}° | {desc}")

def main():
    print("🌤 Welcome to Weather App 🌤")

    favorites = load_favorites()

    while True:
        print("\n1. Current Weather\n2. 5-Day Forecast\n3. Add Favorite\n4. View Favorites\n5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            city = input("Enter city: ")
            unit = input("Unit (metric/imperial): ") or "metric"
            data = get_current_weather(city, unit)
            display_weather(data)
            alerts = data.get("alerts")
            if alerts:
                print("⚠️ Alerts:", alerts)

        elif choice == "2":
            city = input("Enter city: ")
            unit = input("Unit (metric/imperial): ") or "metric"
            data = get_forecast(city, unit)
            display_forecast(data)

        elif choice == "3":
            city = input("City to save: ")
            if city not in favorites:
                favorites.append(city)
                save_favorites(favorites)
                print("✅ Added to favorites.")
            else:
                print("🔁 Already in favorites.")

        elif choice == "4":
            print("\n⭐ Favorite Locations:")
            for city in favorites:
                print("•", city)

        elif choice == "5":
            print("👋 Exiting Weather App.")
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
