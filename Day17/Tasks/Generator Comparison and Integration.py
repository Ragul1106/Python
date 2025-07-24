import timeit

# 1. List vs generator benchmark
list_time = timeit.timeit('[x for x in range(1000000)]', number=100)
gen_time = timeit.timeit('(x for x in range(1000000))', number=100)
print(f"List: {list_time}, Generator: {gen_time}")

# 2. Generator with map
numbers = (x for x in range(5))
squared = map(lambda x: x**2, numbers)

# 3. Generator pipeline
def number_gen(n):
    for i in range(n):
        yield i
def even_filter(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num
def square_mapper(numbers):
    for num in numbers:
        yield num ** 2

pipeline = square_mapper(even_filter(number_gen(10)))

# 4. Command processor
def command_processor():
    while True:
        cmd = yield
        if cmd == 'exit':
            break
        print(f"Processing: {cmd}")

processor = command_processor()
next(processor)  
processor.send('start')
processor.send('load')
processor.send('exit')

# 5. Email validator test
def test_email_validator():
    emails = ["test@example.com", "invalid", "user@domain.org"]
    gen = (email for email in emails if '@' in email)
    assert list(gen) == ["test@example.com", "user@domain.org"]