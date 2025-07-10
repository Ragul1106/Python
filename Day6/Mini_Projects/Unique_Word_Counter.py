def analyze_text(text):
    words = text.split()
    unique_words = set(words)
    longest_word = max(words, key=len)
    return len(words), len(unique_words), longest_word

total, unique, longest = analyze_text("hello world hello python")
print(f"Words: {total}, Unique: {unique}, Longest: '{longest}'")