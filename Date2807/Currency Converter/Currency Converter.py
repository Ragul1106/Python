import requests
import json
import time
from functools import wraps
from typing import Dict, Generator, Optional
from datetime import datetime, timedelta

class CurrencyConverter:
    def __init__(self, api_key: str = "YOUR_API_KEY"):
        self.api_key = api_key
        self.base_url = "https://api.exchangerate-api.com/v4/latest/"
        self.cache_file = "currency_cache.json"
        self.rates: Dict[str, float] = {}
        self.last_updated = 0
        self.cache_expiry = 3600  

        self.load_cached_rates()
    
    def load_cached_rates(self) -> None:
        """Load rates from cache file"""
        try:
            with open(self.cache_file, 'r') as f:
                data = json.load(f)
                if time.time() - data['timestamp'] < self.cache_expiry:
                    self.rates = data['rates']
                    self.last_updated = data['timestamp']
                    print("Loaded rates from cache")
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            pass
    
    def save_cached_rates(self) -> None:
        """Save rates to cache file"""
        data = {
            'rates': self.rates,
            'timestamp': time.time(),
            'base_currency': self.base_currency
        }
        with open(self.cache_file, 'w') as f:
            json.dump(data, f)
    
    @cache_rates
    def fetch_exchange_rates(self, base_currency: str = "USD") -> Dict[str, float]:
        """API call to fetch exchange rates"""
        try:
            response = requests.get(f"{self.base_url}{base_currency}")
            response.raise_for_status()
            data = response.json()
            
            self.rates = data['rates']
            self.base_currency = base_currency
            self.last_updated = data['time_last_updated']
            print(f"Fetched fresh rates from API (Base: {base_currency})")
            
            return self.rates
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to fetch rates: {str(e)}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid API response: {str(e)}")
    
    def get_supported_currencies(self) -> List[str]:
        """List all supported currencies"""
        if not self.rates:
            self.fetch_exchange_rates()
        return list(self.rates.keys())
    
    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Convert between currencies"""
        if not self.rates or time.time() - self.last_updated > self.cache_expiry:
            self.fetch_exchange_rates(from_currency)
        
        try:
            if from_currency == self.base_currency:
                rate = self.rates[to_currency]
            else:

                from_rate = self.rates[from_currency]
                to_rate = self.rates[to_currency]
                rate = to_rate / from_rate
            
            return amount * rate
        except KeyError as e:
            raise ValueError(f"Unsupported currency: {str(e)}")
    
    def get_historical_rates(self, days: int = 7) -> Generator[Dict[str, float], None, None]:
        """Generator: Yield mock historical rates"""
        if not self.rates:
            self.fetch_exchange_rates()
        
        for i in range(days, 0, -1):
            date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
            yield {
                'date': date,
                'rates': {curr: rate * (0.95 + 0.1 * random.random()) 
                          for curr, rate in self.rates.items()}
            }

def cache_rates(func):
    """Decorator: Cache exchange rates to avoid repeated API calls"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):

        if self.rates and time.time() - self.last_updated < self.cache_expiry:
            print("Using cached rates")
            return self.rates

        result = func(self, *args, **kwargs)
        self.save_cached_rates()
        return result
    return wrapper

def main():
    converter = CurrencyConverter(api_key="your_api_key_here")
    
    print("Currency Converter")
    print("==================")
    print(f"Supported currencies: {', '.join(converter.get_supported_currencies()[:5])}...")
    
    while True:
        print("\nMenu:")
        print("1. Convert currency")
        print("2. View historical rates (mock)")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                from_curr = input("From currency (3-letter code): ").upper()
                to_curr = input("To currency (3-letter code): ").upper()
                
                result = converter.convert(amount, from_curr, to_curr)
                print(f"\n{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
            except ValueError as e:
                print(f"Error: {e}")
            except ConnectionError as e:
                print(f"Network error: {e}. Using cached rates if available.")
        
        elif choice == "2":
            days = int(input("Enter number of days for history (max 30): "))
            days = min(max(days, 1), 30)  # Clamp between 1-30
            
            print(f"\nHistorical Rates (mock data for last {days} days):")
            print("Date       | USD       | EUR       | GBP       | JPY")
            print("-" * 45)
            
            for day in converter.get_historical_rates(days):
                rates = day['rates']
                print(f"{day['date']} | {rates['USD']:.4f} | {rates['EUR']:.4f} | {rates['GBP']:.4f} | {rates['JPY']:.4f}")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()