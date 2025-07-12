def count_words(text):
    words = text.split()
    return len(words)

def count_specific_word(text, word):
    return text.lower().split().count(word.lower())

text = input("Enter a paragraph: ")
print(f"\nTotal words: {count_words(text)}")

word = input("\nEnter word to count: ")
print(f"'{word}' appears {count_specific_word(text, word)} times")