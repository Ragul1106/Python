sentence = input("Enter a sentence: ")
reversed_words = [word[::-1] for word in sentence.split()]
print(' '.join(reversed_words))