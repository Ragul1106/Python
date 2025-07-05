sentence = input("Enter a sentence: ")
result = ""
for char in sentence:
    if char.lower() in "aeiou":
        continue
    result += char
print("Filtered Sentence:", result)