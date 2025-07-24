def lazy_squares(numbers):
    for num in numbers:
        yield num ** 2

print("\nLazy Squares:")
squares = lazy_squares([1, 2, 3])
print(next(squares))
print(next(squares))