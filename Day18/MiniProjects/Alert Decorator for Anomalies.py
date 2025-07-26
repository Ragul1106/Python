from functools import wraps

def alert_on_threshold(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f"ALERT: Value {result} exceeds threshold {threshold}")
            return result
        return wrapper
    return decorator

@alert_on_threshold(100)
def read_sensor():
    import random
    return random.randint(80, 120)

read_sensor()