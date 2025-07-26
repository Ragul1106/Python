from functools import wraps

def validate_types(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg, type_ in zip(args, types):
                if not isinstance(arg, type_):
                    raise TypeError(f"Expected {type_}, got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, int)
def add(a, b):
    return a + b

add(1, 2)  
add("1", 2)  