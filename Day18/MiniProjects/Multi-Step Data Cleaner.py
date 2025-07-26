from functools import wraps

def remove_nulls(func):
    @wraps(func)
    def wrapper(data):
        cleaned = [x for x in data if x is not None]
        return func(cleaned)
    return wrapper

def strip_whitespace(func):
    @wraps(func)
    def wrapper(data):
        stripped = [x.strip() if isinstance(x, str) else x for x in data]
        return func(stripped)
    return wrapper

def lowercase_strings(func):
    @wraps(func)
    def wrapper(data):
        lower = [x.lower() if isinstance(x, str) else x for x in data]
        return func(lower)
    return wrapper

@lowercase_strings
@strip_whitespace
@remove_nulls
def process_data(data):
    return data

print(process_data(["  TEST  ", None, "Value", 123]))