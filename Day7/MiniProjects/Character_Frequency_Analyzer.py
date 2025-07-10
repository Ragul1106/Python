text = input("Enter text: ").lower()
for vowel in 'aeiou':
    print(f"{vowel}: {text.count(vowel)}")