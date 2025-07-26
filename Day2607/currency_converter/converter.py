import requests
from datetime import datetime

API_URL = "https://api.exchangerate.host"

def get_rate(from_currency, to_currency, date=None):
    if date:
        url = f"{API_URL}/{date}"
    else:
        url = f"{API_URL}/latest"

    params = {
        "base": from_currency,
        "symbols": to_currency
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        return data["rates"][to_currency]
    except:
        return None

def convert_amount(amount, from_currency, to_currency):
    rate = get_rate(from_currency, to_currency)
    if rate:
        return amount * rate, rate
    return None, None
