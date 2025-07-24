# 1. Generator for numbers 1-10
def numbers_to_10():
    for i in range(1, 11):
        yield i

# 2. Even numbers generator
def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i

# 3. Squares generator
def squares(n):
    for i in range(1, n+1):
        yield i * i

# 4. String character generator
def char_generator(text):
    for char in text:
        yield char

# 5. Vowel generator
def vowel_generator(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in text.lower():
        if char in vowels:
            yield char

# 6. Manual iteration with next()
letters = (chr(97+i) for i in range(5))  # Generator expression
print(next(letters))  # 'a'
print(next(letters))  # 'b'

# 7. StopIteration example
def limited_gen():
    yield 1
    yield 2
gen = limited_gen()
print(next(gen))  # 1
print(next(gen))  # 2
try:
    print(next(gen)) 
except StopIteration:
    print("Generator exhausted")

# 8. Prime number generator
def primes(limit):
    for num in range(2, limit+1):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            yield num

# 9. Memory comparison
import sys
def list_func(n):
    return [i for i in range(n)]
def gen_func(n):
    return (i for i in range(n))
print(sys.getsizeof(list_func(100000)))  
print(sys.getsizeof(gen_func(100000)))   

# 10. Positive numbers filter
def positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            yield num