known_words = {'the', 'and', 'of'}
article_words = {'the', 'quick', 'brown', 'fox'}

new_words = article_words - known_words
print("New words to learn:", new_words)