# 1. Word-by-word generator
def word_generator(text):
    for word in text.split():
        yield word

# 2. Cumulative sum generator
def cumulative_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total

# 3. Range implementation
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    while start < stop:
        yield start
        start += step

# 4. Flatten nested lists
def flatten(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item

# 5. Factorial generator
def factorial_gen(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result

# 6. Powers of 2
def powers_of_two(limit):
    power = 1
    while power <= limit:
        yield power
        power *= 2

# 7. Fibonacci generator
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 8. Even number filter
def even_filter(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

# 9. Chained generators
def number_gen(n):
    for i in range(n):
        yield i
def square_gen(numbers):
    for num in numbers:
        yield num * num
chain = square_gen(number_gen(5))

# 10. Reverse string generator
def reverse_string(text):
    for char in reversed(text):
        yield char