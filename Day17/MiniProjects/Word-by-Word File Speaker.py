import string

def word_reader(filename):
    with open(filename) as file:
        for line in file:

            words = line.translate(str.maketrans('', '', string.punctuation)).split()
            for word in words:
                yield word.lower()
                
                yield None  


# reader = word_reader('sample.txt')
# for word in reader:
#     if word is not None:
#         print(word, end=' ', flush=True)
#     time.sleep(0.2)  # Typing effect