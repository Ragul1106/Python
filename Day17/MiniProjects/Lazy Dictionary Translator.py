def english_to_tamil_translator(words):
    dictionary = {
        "hello": "வணக்கம்",
        "world": "உலகம்",
        "python": "பைதான்"
    }
    for word in words:
        if word.lower() in dictionary:
            yield word
            yield dictionary[word.lower()]
        else:
            yield f"Unknown word: {word}"

words = ["Hello", "World", "Java", "Python"]
translator = english_to_tamil_translator(words)

for translation in translator:
    print(translation)