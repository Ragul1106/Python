from functools import wraps

def html_wrapper(tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator

@html_wrapper("div")
@html_wrapper("h1")
def get_title():
    return "Welcome"

print(get_title())  