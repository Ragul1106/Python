text = input("Enter a sentence: ")
vowels = consonants = digits = specials = 0
for char in text:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    else:
        specials += 1
print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}, Special Chars: {specials}")