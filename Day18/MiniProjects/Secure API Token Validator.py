from functools import wraps

def validate_token(expected_token):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = kwargs.get('token')
            if token != expected_token:
                raise ValueError("Invalid API token")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_token("secret123")
def api_request(**kwargs):
    return "Sensitive data"

api_request(token="secret123")  
api_request(token="wrong")  