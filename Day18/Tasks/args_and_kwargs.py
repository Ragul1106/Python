# 1. Argument logger
def args_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Positional args: {args}")
        print(f"Keyword args: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# 2. Argument summer
def args_summer(func):
    def wrapper(*args, **kwargs):
        total = sum(args) + sum(kwargs.values())
        print(f"Sum of arguments: {total}")
        return func(*args, **kwargs)
    return wrapper

# 3. Type validator
def type_validator(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, type_) in enumerate(zip(args, types)):
                if not isinstance(arg, type_):
                    raise ValueError(f"Argument {i} must be {type_}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 4. Non-empty string validator
def non_empty_string(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str) and not arg.strip():
                raise ValueError("String argument cannot be empty")
        return func(*args, **kwargs)
    return wrapper

# 5. Keyword argument enforcer
def requires_kwarg(func):
    def wrapper(*args, **kwargs):
        if not kwargs:
            raise ValueError("At least one keyword argument required")
        return func(*args, **kwargs)
    return wrapper

# 6. Integer-only arguments
def int_only(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("All arguments must be integers")
        return func(*args, **kwargs)
    return wrapper

# 7. List reverser
def reverse_list_args(func):
    def wrapper(*args, **kwargs):
        new_args = [arg[::-1] if isinstance(arg, list) else arg for arg in args]
        return func(*new_args, **kwargs)
    return wrapper

# 8. String lowercase converter
def lowercase_strings(func):
    def wrapper(*args, **kwargs):
        new_args = [arg.lower() if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {k: v.lower() if isinstance(v, str) else v for k, v in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper

# 9. Float rounder
def round_floats(places=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, float):
                return round(result, places)
            return result
        return wrapper
    return decorator

# 10. Function blocker
def block_execution(func):
    def wrapper(*args, block=False, **kwargs):
        if block:
            print("Execution blocked!")
            return None
        return func(*args, **kwargs)
    return wrapper