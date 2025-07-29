import feedparser
import time
from functools import wraps
import os

def update_check(func):
    last_updated = {}

    @wraps(func)
    def wrapper(self, url):
        feed = feedparser.parse(url)
        updated = feed.get('updated', '')
        if last_updated.get(url) == updated:
            print("No new updates.")
            return []
        last_updated[url] = updated
        return func(self, url)
    return wrapper

class Feed:
    def __init__(self, url, save_path="rss_articles.txt"):
        self.url = url
        self.save_path = save_path

    @update_check
    def fetch_feed(self, url):
        try:
            feed = feedparser.parse(url)
            if feed.bozo:
                raise ValueError("Invalid RSS feed or parsing error.")
            return self._article_generator(feed.entries)
        except Exception as e:
            print(f"Error fetching feed: {e}")
            return []

    def _article_generator(self, entries):
        for entry in entries:
            yield {
                'title': entry.get('title'),
                'link': entry.get('link'),
                'published': entry.get('published', 'N/A'),
                'summary': entry.get('summary', '')
            }

    def save_articles(self, articles):
        try:
            with open(self.save_path, 'a', encoding='utf-8') as f:
                for article in articles:
                    f.write(f"Title: {article['title']}\n")
                    f.write(f"Link: {article['link']}\n")
                    f.write(f"Published: {article['published']}\n")
                    f.write(f"Summary: {article['summary']}\n")
                    f.write("="*60 + "\n")
            print(f"Articles saved to {self.save_path}")
        except Exception as e:
            print(f"Error saving articles: {e}")

def main():
    url = input("Enter RSS feed URL: ").strip()
    feed = Feed(url)

    while True:
        print("\nChecking for new articles...\n")
        articles = feed.fetch_feed(url)
        if articles:
            feed.save_articles(articles)
        else:
            print("No articles to save.")
        try:
            time.sleep(30)  
        except KeyboardInterrupt:
            print("\nExiting RSS Feed Reader.")
            break

if __name__ == "__main__":
    main()
