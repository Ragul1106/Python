from pytube import YouTube
from functools import wraps
import os
import sys

def progress_bar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Download starting...")
        result = func(*args, **kwargs)
        print("Download completed!")
        return result
    return wrapper

class Downloader:
    def __init__(self, url, save_path='downloads'):
        self.url = url.strip()
        self.save_path = save_path
        os.makedirs(save_path, exist_ok=True)

    @progress_bar
    def download_video(self):
        try:
            yt = YouTube(self.url, on_progress_callback=self._show_progress)
            stream = yt.streams.get_highest_resolution()
            print(f"Title: {yt.title}")
            stream.download(output_path=self.save_path)
        except Exception as e:
            print(f"Error: {e}")

    def _show_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        progress = (bytes_downloaded / total_size) * 100
        sys.stdout.write(f"\rDownloading... {progress:.2f}%")
        sys.stdout.flush()

def main():
    url = input("Enter YouTube Video URL: ")
    downloader = Downloader(url)
    downloader.download_video()

if __name__ == "__main__":
    main()
