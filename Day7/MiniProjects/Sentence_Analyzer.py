sentence = input("Enter a sentence: ")
vowels = "aeiou"

print(f"First character: {sentence[0]}")
print(f"Last character: {sentence[-1]}")
print(f"First space at position: {sentence.find(' ')}")
print(f"Total vowels: {sum(1 for c in sentence.lower() if c in vowels)}")
print(f"Total spaces: {sentence.count(' ')}")