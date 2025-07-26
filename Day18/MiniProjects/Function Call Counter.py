from functools import wraps

def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"{func.__name__} called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0
    wrapper.reset = lambda: setattr(wrapper, 'count', 0)
    return wrapper

@call_counter
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello.reset()
say_hello()