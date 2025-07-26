from functools import wraps
from datetime import datetime

def api_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            status = "Success"
            return result
        except Exception as e:
            status = f"Fail: {str(e)}"
            raise
        finally:
            print(f"[{datetime.now()}] {func.__name__} - Args: {args}, Kwargs: {kwargs} - Status: {status}")
    return wrapper

@api_logger
def fetch_data(api_endpoint, params=None):
    if "error" in str(api_endpoint):
        raise ValueError("API Error")
    return {"data": "sample"}

fetch_data("/users") 
fetch_data("/error")  