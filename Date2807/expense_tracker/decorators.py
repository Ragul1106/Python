from functools import wraps
from utils import is_valid_amount

def validate_input(func):
    @wraps(func)
    def wrapper(amount, category, *args, **kwargs):
        if not is_valid_amount(amount):
            print("❌ Invalid amount. Please enter a number.")
            return
        if not category.strip():
            print("❌ Category cannot be empty.")
            return
        return func(amount, category, *args, **kwargs)
    return wrapper
