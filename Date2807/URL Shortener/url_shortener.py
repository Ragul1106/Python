import os
import json
import random
import string
from datetime import datetime, timedelta
from functools import lru_cache, wraps

# ========== Decorator ==========
def cache(func):
    _cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in _cache:
            print("🔁 Retrieved from cache.")
            return _cache[args]
        result = func(*args)
        _cache[args] = result
        return result
    return wrapper

# ========== OOP ==========
class URLShortener:
    def __init__(self, db_path="url_data/urls.json"):
        self.db_path = db_path
        self.urls = {}
        self.expiry_days = 30
        self._load_data()

    def _load_data(self):
        if not os.path.exists(self.db_path):
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            with open(self.db_path, 'w') as f:
                json.dump({}, f)
        with open(self.db_path, 'r') as f:
            self.urls = json.load(f)

    def _save_data(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.urls, f, indent=4)

    def _generate_shortcode(self, length=6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def _is_valid_url(self, url):
        return url.startswith("http://") or url.startswith("https://")

    def shorten(self, original_url):
        if not self._is_valid_url(original_url):
            raise ValueError("Invalid URL. Must start with http:// or https://")
        
        shortcode = self._generate_shortcode()
        while shortcode in self.urls:
            shortcode = self._generate_shortcode()

        self.urls[shortcode] = {
            "original_url": original_url,
            "created_at": datetime.now().isoformat()
        }
        self._save_data()
        print(f"✅ Shortened URL: {shortcode}")
        return shortcode

    @cache
    def redirect(self, shortcode):
        url_data = self.urls.get(shortcode)
        if url_data:
            print(f"🔗 Redirecting to: {url_data['original_url']}")
            return url_data["original_url"]
        else:
            print("❌ URL not found.")
            return None

    def delete(self, shortcode):
        if shortcode in self.urls:
            del self.urls[shortcode]
            self._save_data()
            print("🗑️ Shortened URL deleted.")
        else:
            print("❌ URL not found.")

    def list_urls(self):
        if not self.urls:
            print("📭 No URLs shortened yet.")
        for code, data in self.urls.items():
            print(f"🔸 {code} -> {data['original_url']} (Created: {data['created_at']})")

    # ========== Generator ==========
    def expired_urls(self):
        now = datetime.now()
        for code, data in self.urls.items():
            created = datetime.fromisoformat(data['created_at'])
            if (now - created).days > self.expiry_days:
                yield code, data

# ========== Menu ==========
def menu():
    shortener = URLShortener()
    
    while True:
        print("\n🌐 URL Shortener Menu")
        print("1. Shorten URL")
        print("2. Redirect URL")
        print("3. Delete URL")
        print("4. List All URLs")
        print("5. Show Expired URLs (30+ days)")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            url = input("Enter full URL: ")
            try:
                shortener.shorten(url)
            except ValueError as e:
                print(f"⚠️ {e}")
        elif choice == '2':
            code = input("Enter short code: ")
            shortener.redirect(code)
        elif choice == '3':
            code = input("Enter short code to delete: ")
            shortener.delete(code)
        elif choice == '4':
            shortener.list_urls()
        elif choice == '5':
            print("🧾 Expired URLs (older than 30 days):")
            for code, data in shortener.expired_urls():
                print(f"⏳ {code} -> {data['original_url']} (Created: {data['created_at']})")
        elif choice == '6':
            print("👋 Exiting URL Shortener.")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
