import requests

API_KEY = "043c51d5d245a75d77720a6c99b19452"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city_weather_data = {}

visited_cities = set()

def fetch_weather(city_name):
    if city_name.lower() in visited_cities:
        print(f"\nWeather for '{city_name}' already fetched.")
        return

    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] == 200:
            lat = data["coord"]["lat"]
            lon = data["coord"]["lon"]
            coord = (lat, lon)

            weather_info = {
                "city": city_name,
                "temperature": data["main"]["temp"],
                "condition": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"]
            }

            city_weather_data[coord] = weather_info
            visited_cities.add(city_name.lower())

            print_weather(coord)

        else:
            print("\nCity not found.")

    except Exception as e:
        print("Error:", e)

def print_weather(coord):
    if coord in city_weather_data:
        info = city_weather_data[coord]
        print(f"\n📍 Weather for {info['city']} (Lat: {coord[0]}, Lon: {coord[1]})")
        print(f"🌡️  Temperature: {info['temperature']}°C")
        print(f"☁️  Condition: {info['condition']}")
        print(f"💧 Humidity: {info['humidity']}%")
    else:
        print("No data for given coordinates.")
