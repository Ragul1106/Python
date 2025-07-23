import os
from collections import Counter

def analyze_file(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            char_count = len(text)
            most_common = Counter(words).most_common(1)[0]

            print("\n📊 Text File Analysis:")
            print(f"Total Words       : {word_count}")
            print(f"Total Characters  : {char_count}")
            print(f"Most Frequent Word: '{most_common[0]}' ({most_common[1]} times)")
    except FileNotFoundError:
        print("❌ File not found. Please enter a valid file path.")
    except Exception as e:
        print("❌ Error reading file:", str(e))

def main():
    print("=== Text File Analyzer ===")
    filename = input("Enter file name (with .txt extension): ").strip()
    analyze_file(filename)

if __name__ == "__main__":
    main()
