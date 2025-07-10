text = input("Enter a paragraph: ").lower()
words = text.split()

for word in set(words):
    print(f"'{word}': {words.count(word)} times")

print(f"\nTotal words: {len(words)}")