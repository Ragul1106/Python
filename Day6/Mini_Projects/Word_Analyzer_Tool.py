def word_analyzer(*words):
    # Print word lengths using map
    print("Word lengths:", list(map(len, words)))
    
    # Convert to uppercase using lambda
    upper_words = list(map(lambda x: x.upper(), words))
    print("Uppercase words:", upper_words)
    
    # Most frequent character in each word
    for word in words:
        freq_char = max(set(word), key=word.count)
        print(f"Most frequent in '{word}': '{freq_char}'")

word_analyzer("hello", "python", "programming")