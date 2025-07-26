from functools import wraps

def validate_numeric_input(func):
    @wraps(func)
    def wrapper(*args):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("All arguments must be numeric")
        return func(*args)
    return wrapper

def log_output(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        print(f"{func.__name__}{args} = {result}")
        return result
    return wrapper

def timeit(func):
    @wraps(func)
    def wrapper(*args):
        import time
        start = time.perf_counter()
        result = func(*args)
        duration = time.perf_counter() - start
        print(f"Execution time: {duration:.6f}s")
        return result
    return wrapper

@timeit
@log_output
@validate_numeric_input
def add(a, b):
    return a + b

@timeit
@log_output
@validate_numeric_input
def multiply(a, b):
    return a * b

add(2, 3)
multiply(4, 5)