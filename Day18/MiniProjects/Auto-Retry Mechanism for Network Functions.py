import time
from functools import wraps

def retry(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts <= max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {str(e)}")
                    if attempts > max_retries:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_retries=2, delay=0.5)
def unstable_network_call():
    if time.time() % 2 > 1: 
        raise ConnectionError("Network issue")
    return "Success"

unstable_network_call()