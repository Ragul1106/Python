import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"⏱️ Function '{func.__name__}' executed in {time.time() - start:.4f} sec")
        return result
    return wrapper
