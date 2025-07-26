from functools import wraps

def secure_property(log_access=True):
    def decorator(func):
        @property
        @wraps(func)
        def wrapper(self):
            if log_access:
                print(f"Accessing secure data from {func.__name__}")
            return func(self)
        
        @wrapper.setter
        def wrapper(self, value):
            raise AttributeError("Secure data cannot be modified")
        
        return wrapper
    return decorator

class SecureSystem:
    def __init__(self):
        self._api_key = "secret123"
    
    @secure_property()
    def api_key(self):
        return "***" + self._api_key[-3:]

system = SecureSystem()
print(system.api_key)  
system.api_key = "new"  