from functools import wraps
from datetime import datetime

def file_logger(level="INFO"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open("log.txt", "a") as f:
                log_entry = (
                    f"[{datetime.now()}] {level} - "
                    f"{func.__name__} - Args: {args}, Kwargs: {kwargs} - "
                    f"Result: {result}\n"
                )
                f.write(log_entry)
            return result
        return wrapper
    return decorator

@file_logger("DEBUG")
def process_data(data):
    return data.upper()

process_data("test")