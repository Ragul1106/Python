word = input("Enter a word: ").lower()
frequency = {}

for char in word:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\nCharacter Frequency:")
for char, count in frequency.items():
    print(f"{char}: {count}")