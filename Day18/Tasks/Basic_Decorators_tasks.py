# 1. Basic start message decorator
def start_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        return func(*args, **kwargs)
    return wrapper

# 2. Function name printer
def name_printer(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 3. Call counter
def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Function called {wrapper.count} times")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

# 4. Square return value
def square_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2
    return wrapper

# 5. Uppercase return
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result).upper()
    return wrapper

# 6. Argument and return logger
def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Args: {args}, Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

# 7. Before-after logger
def before_after_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Before {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After {func.__name__}")
        return result
    return wrapper

# 8. Exception handler
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {str(e)}")
            return None
    return wrapper

# 9. Execution timer
import time
def execution_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

# 10. Datetime logger
from datetime import datetime
def datetime_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Current datetime: {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper