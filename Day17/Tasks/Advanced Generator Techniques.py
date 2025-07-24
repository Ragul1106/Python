# 1. Infinite multiples of 5
def multiples_of_5():
    num = 0
    while True:
        yield num
        num += 5

# 2. Chunk generator
def chunker(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i+size]

# 3. Sorted names generator
def sorted_names(names):
    for name in sorted(names):
        yield name

# 4. Reversed file lines
def reversed_lines(filename):
    with open(filename) as file:
        for line in reversed(list(file)):
            yield line.strip()

# 5. Countdown generator
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# 6. Logging generator
def logged_gen():
    print("Starting")
    yield 1
    print("Yielding 2")
    yield 2
    print("Done")

# 7. Generator with send()
def doubler():
    result = None
    while True:
        value = yield result
        result = value * 2

# 8. Generator with return
def gen_with_return():
    yield 1
    yield 2
    return "Done"
gen = gen_with_return()
try:
    while True:
        print(next(gen))
except StopIteration as e:
    print(e.value)  # "Done"

# 9. CSV line reader
def csv_reader(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip().split(',')

# 10. Yield counter
def counting_gen():
    count = 0
    while True:
        yield count
        count += 1