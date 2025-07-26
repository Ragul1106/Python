from functools import wraps

def notification(header, footer):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(header)
            result = func(*args, **kwargs)
            print(footer)
            return result
        return wrapper
    return decorator

@notification("=== SYSTEM NOTIFICATION ===", "=== END ===")
def system_update(message):
    print(message)

system_update("Server maintenance scheduled")