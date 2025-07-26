import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"{func.__name__} executed in {duration:.4f} seconds")
        return result
    return wrapper

@timeit
def heavy_computation(n):
    return sum(i*i for i in range(n))

heavy_computation(1000000)