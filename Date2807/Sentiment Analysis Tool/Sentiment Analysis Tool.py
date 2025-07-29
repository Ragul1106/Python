from textblob import TextBlob
from functools import wraps
import time

def cache_results(func):
    cache = {}
    @wraps(func)
    def wrapper(self, text):
        if text in cache:
            print("Using cached result.")
            return cache[text]
        result = func(self, text)
        cache[text] = result
        return result
    return wrapper

class Analyzer:
    def __init__(self):
        self.results_history = []

    @cache_results
    def analyze_sentiment(self, text):
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            sentiment = self.get_sentiment_label(polarity)
            result = {
                'text': text,
                'polarity': polarity,
                'subjectivity': subjectivity,
                'sentiment': sentiment
            }
            self.results_history.append(result)
            return result
        except Exception as e:
            print(f"API/Processing Error: {e}")
            return None

    def get_sentiment_label(self, polarity):
        if polarity > 0.2:
            return "Positive"
        elif polarity < -0.2:
            return "Negative"
        else:
            return "Neutral"

    def print_history(self):
        print("\n--- Sentiment History ---")
        for i, r in enumerate(self.results_history, 1):
            print(f"{i}. {r['sentiment']} | Polarity: {r['polarity']:.2f} | Text: {r['text'][:50]}...")

def main():
    analyzer = Analyzer()
    print("Sentiment Analysis Tool (type 'exit' to quit)\n")
    while True:
        text = input("Enter text to analyze: ")
        if text.lower() == 'exit':
            break
        if text.strip():
            result = analyzer.analyze_sentiment(text)
            if result:
                print(f"Sentiment: {result['sentiment']}")
                print(f"Polarity: {result['polarity']:.2f}, Subjectivity: {result['subjectivity']:.2f}")
    analyzer.print_history()

if __name__ == "__main__":
    main()
