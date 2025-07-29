import requests
from decorators import retry
from weather import Weather

API_KEY = "043c51d5d245a75d77720a6c99b19452"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@retry
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}")
    data = response.json()
    weather = Weather(
        temp=data["main"]["temp"],
        humidity=data["main"]["humidity"],
        description=data["weather"][0]["description"].title()
    )
    return weather, data
