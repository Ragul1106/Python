def count_characters(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

text = input("Enter a sentence: ")
frequency = count_characters(text)

print("\nCharacter Frequency:")
for char, count in sorted(frequency.items()):
    print(f"{char}: {count}")