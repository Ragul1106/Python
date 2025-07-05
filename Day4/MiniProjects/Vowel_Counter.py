sentence = input("Enter a sentence: ")
vowels = 'aeiou'
vowel_count = 0
for char in sentence.lower():
    if char in vowels:
        vowel_count += 1
print("Total vowels:", vowel_count)