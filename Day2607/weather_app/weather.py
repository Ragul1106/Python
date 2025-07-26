import requests
import json

API_KEY = "043c51d5d245a75d77720a6c99b19452"
BASE_URL = "https://api.openweathermap.org/data/2.5/"

def get_current_weather(city, unit="metric"):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units={unit}"
    response = requests.get(url)
    return response.json()

def get_forecast(city, unit="metric"):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units={unit}"
    response = requests.get(url)
    return response.json()

def load_favorites():
    try:
        with open("favorites.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_favorites(favs):
    with open("favorites.json", "w") as f:
        json.dump(favs, f, indent=2)
