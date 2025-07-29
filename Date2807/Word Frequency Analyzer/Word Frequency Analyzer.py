import os
from collections import Counter
import string

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def count_words(text):
    words = text.split()
    return Counter(words)

def get_top_words(counter, n=10):
    for word, count in counter.most_common(n):
        yield word, count

def save_report(counter, filename="word_report.txt"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for word, count in counter.most_common():
                f.write(f"{word}: {count}\n")
        print(f"Report saved to {filename}")
    except Exception as e:
        print(f"Failed to save report: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path of the text file to analyze: ")
    text = read_file(file_path)
    
    if text:
        cleaned = clean_text(text)
        word_counts = count_words(cleaned)

        print("\nTop 10 Words:")
        for word, count in get_top_words(word_counts, 10):
            print(f"{word}: {count}")

        save_report(word_counts)
