from functools import wraps
import random
import time

def log_email(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Sending email to {args[0]}...")
        return func(*args, **kwargs)
    return wrapper

def retry_email(max_retries=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts <= max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed, retrying...")
                    if attempts > max_retries:
                        raise
                    time.sleep(1)
        return wrapper
    return decorator

@retry_email()
@log_email
def send_email(to):
    if random.random() < 0.7: 
        raise RuntimeError("SMTP Error")
    return "Email sent"

send_email("user@example.com")