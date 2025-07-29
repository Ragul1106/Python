import re
import time
from collections import defaultdict
from functools import wraps
from typing import Dict, Generator, Tuple

def time_execution(func):
    """Decorator to measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

class WordCounter:
    def __init__(self, filename: str):
        self.filename = filename
        self.word_counts: Dict[str, int] = defaultdict(int)
        self.line_count = 0
        self.char_count = 0
        self.total_words = 0
    
    def read_file(self) -> Generator[str, None, None]:
        """Generator: Yield lines from the file one by one"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    yield line
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{self.filename}' was not found")
        except UnicodeDecodeError:
            raise UnicodeDecodeError("Could not decode the file with UTF-8 encoding")

    def clean_word(self, word: str) -> str:
        """Clean a word by removing punctuation and converting to lowercase"""
        return re.sub(r'[^\w\s]', '', word).lower()

    @time_execution
    def analyze_file(self) -> None:
        """Analyze the file and count words, lines, and characters"""
        try:
            for line in self.read_file():
                self.line_count += 1
                self.char_count += len(line)
                
                words = line.split()
                self.total_words += len(words)
                
                for word in words:
                    cleaned_word = self.clean_word(word)
                    if cleaned_word:  
                        self.word_counts[cleaned_word] += 1
            
            print("\nFile analysis complete!")
        except Exception as e:
            print(f"\nError analyzing file: {e}")

    def count_words(self) -> int:
        """Return the total number of words in the file"""
        return self.total_words

    def most_common_word(self, n: int = 1) -> Tuple[str, int]:
        """Return the n most common words and their counts"""
        sorted_words = sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:n]

    def display_stats(self) -> None:
        """Display file statistics"""
        print("\n=== File Statistics ===")
        print(f"File: {self.filename}")
        print(f"Lines: {self.line_count}")
        print(f"Words: {self.count_words()}")
        print(f"Characters: {self.char_count}")
        
        if self.word_counts:
            common_word, count = self.most_common_word()[0]
            print(f"\nMost common word: '{common_word}' (appears {count} times)")
        
        print("=" * 22)

    def word_generator(self) -> Generator[str, None, None]:
        """Generator: Yield words one by one"""
        for word, count in self.word_counts.items():
            for _ in range(count):
                yield word

def main():
    print("Word Counter - File Analysis Tool")
    print("================================\n")
    
    while True:
        filename = input("Enter the path to a text file (or 'quit' to exit): ").strip()
        
        if filename.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        
        try:
            counter = WordCounter(filename)
            counter.analyze_file()
            counter.display_stats()
            
         
            if input("\nShow first 10 words? (y/n): ").lower() == 'y':
                print("\nFirst 10 words from generator:")
                for i, word in enumerate(counter.word_generator(), 1):
                    if i > 10:
                        break
                    print(f"{i}. {word}")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()