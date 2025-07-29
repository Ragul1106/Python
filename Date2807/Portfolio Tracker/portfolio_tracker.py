import yfinance as yf
import json
import os
from functools import lru_cache


def cache(func):
    return lru_cache(maxsize=100)(func)

class Portfolio:
    def __init__(self, file_path="portfolio.json"):
        self.stocks = {}  
        self.file_path = file_path
        self.load_portfolio()

    def add_stock(self, symbol, shares):
        symbol = symbol.upper()
        self.stocks[symbol] = self.stocks.get(symbol, 0) + shares
        self.save_portfolio()

    def remove_stock(self, symbol):
        symbol = symbol.upper()
        if symbol in self.stocks:
            del self.stocks[symbol]
            self.save_portfolio()

    def save_portfolio(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump(self.stocks, f)
        except Exception as e:
            print(f"❌ Error saving portfolio: {e}")

    def load_portfolio(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    self.stocks = json.load(f)
            except Exception as e:
                print(f"❌ Error loading portfolio: {e}")

    def show_portfolio(self):
        print("\n📈 Your Portfolio:")
        total_value = 0
        for symbol, shares in self.stocks.items():
            price = get_stock_price(symbol)
            if price is not None:
                value = shares * price
                total_value += value
                print(f"{symbol}: {shares} shares × ₹{price:.2f} = ₹{value:.2f}")
            else:
                print(f"{symbol}: Failed to fetch price.")
        print(f"🧾 Total Portfolio Value: ₹{total_value:.2f}")


@cache
def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if not data.empty:
            return data['Close'][-1]
        else:
            return None
    except Exception as e:
        print(f"❌ API error for {symbol}: {e}")
        return None

def main():
    portfolio = Portfolio()
    while True:
        print("\n🔘 1. Add Stock\n🔘 2. Remove Stock\n🔘 3. View Portfolio\n🔘 4. Exit")
        choice = input("Choose: ").strip()
        if choice == '1':
            symbol = input("Stock Symbol (e.g. AAPL): ")
            try:
                shares = float(input("No. of Shares: "))
                portfolio.add_stock(symbol, shares)
                print("✅ Stock added!")
            except ValueError:
                print("❌ Invalid number of shares.")
        elif choice == '2':
            symbol = input("Stock Symbol to remove: ")
            portfolio.remove_stock(symbol)
            print("✅ Stock removed!")
        elif choice == '3':
            portfolio.show_portfolio()
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
