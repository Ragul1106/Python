import time
from functools import wraps

def throttle(max_calls_per_minute):
    def decorator(func):
        calls = []
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls.append(now)

            calls[:] = [call for call in calls if now - call < 60]
            
            if len(calls) > max_calls_per_minute:
                raise RuntimeError(f"Rate limit exceeded: {max_calls_per_minute} calls/minute")
                
            return func(*args, **kwargs)
        return wrapper
    return decorator

@throttle(3)
def api_call():
    print("API call successful")

for _ in range(5):  
    try:
        api_call()
    except RuntimeError as e:
        print(e)
    time.sleep(20)  