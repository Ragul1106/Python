import os
import requests
from PIL import Image
from io import BytesIO

class Downloader:
    def __init__(self, download_dir="downloads"):
        self.download_dir = download_dir
        os.makedirs(self.download_dir, exist_ok=True)
        self.queue = []

    def add_url(self, url):
        self.queue.append(url)

    def download_generator(self):
        for idx, url in enumerate(self.queue, start=1):
            yield from self._download_one(idx, url)

    def _download_one(self, idx, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            yield (idx, url, False, f"Request failed: {e}")
            return

        try:
            img = Image.open(BytesIO(response.content))
        except Exception:
            yield (idx, url, False, "Invalid image data")
            return

        filename = os.path.join(self.download_dir, f"image_{idx}.{img.format.lower()}")
        try:
            img.save(filename)
            yield (idx, url, True, filename)
        except Exception as e:
            yield (idx, url, False, f"Save error: {e}")


def main():
    print("🖼️ Image Downloader")
    dl = Downloader()

    print("Enter image URLs (type 'done' when finished):")
    while True:
        url = input("URL: ").strip()
        if url.lower() in ('done', 'exit'):
            break
        dl.add_url(url)

    print("\nDownloading images...")
    for idx, url, success, info in dl.download_generator():
        if success:
            print(f"[{idx}] ✅ Downloaded to {info}")
        else:
            print(f"[{idx}] ❌ Failed ({info})")

if __name__ == "__main__":
    main()
