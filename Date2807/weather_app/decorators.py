import time
from functools import wraps

def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for attempt in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(1)
        print("❌ All retry attempts failed.")
    return wrapper
