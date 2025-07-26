import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_trend(base, target, days=7):
    end = datetime.today()
    start = end - timedelta(days=days)

    url = f"https://api.exchangerate.host/timeseries"
    params = {
        "start_date": start.strftime("%Y-%m-%d"),
        "end_date": end.strftime("%Y-%m-%d"),
        "base": base,
        "symbols": target
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        dates = sorted(data["rates"].keys())
        rates = [data["rates"][d][target] for d in dates]

        plt.plot(dates, rates, marker='o')
        plt.title(f"{base} to {target} - Last {days} Days")
        plt.xlabel("Date")
        plt.ylabel("Exchange Rate")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except:
        print("Failed to load data for plotting.")
