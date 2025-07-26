import time
from functools import wraps

# 1. Rate limiter
class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
        
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            self.calls = [t for t in self.calls if t > now - self.period]
            if len(self.calls) >= self.max_calls:
                raise RuntimeError("Rate limit exceeded")
            self.calls.append(now)
            return func(*args, **kwargs)
        return wrapper

# 2. Retry decorator
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

# 3. Timing tracker
def time_tracker(log_list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            log_list.append((func.__name__, duration))
            return result
        return wrapper
    return decorator

# 4. API token checker
def require_api_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get('token')
        if token != "valid_token":
            raise PermissionError("Invalid API token")
        return func(*args, **kwargs)
    return wrapper

# 5. Encryption decorator
def encrypt_result(key):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            encrypted = ''.join(chr(ord(c) ^ key) for c in str(result))
            return encrypted
        return wrapper
    return decorator