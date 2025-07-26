# 1. Class-based logger
class ClassLogger:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        print(f"Before {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"After {self.func.__name__}")
        return result

# 2. Memoization decorator
class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

# 3. Instance counter
class InstanceCounter:
    count = 0
    
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        InstanceCounter.count += 1
        print(f"Instance count: {InstanceCounter.count}")
        return self.func(*args, **kwargs)

# 4. Classmethod with logger
def logged_classmethod(func):
    @classmethod
    def wrapper(cls, *args, **kwargs):
        print(f"Calling classmethod {func.__name__}")
        return func(cls, *args, **kwargs)
    return wrapper

# 5. Property with logger
def logged_property(func):
    @property
    def wrapper(self):
        print(f"Accessing property {func.__name__}")
        return func(self)
    return wrapper