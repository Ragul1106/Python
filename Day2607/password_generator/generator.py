import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    char_set = ""
    if use_upper:
        char_set += string.ascii_uppercase
    if use_lower:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation

    if not char_set:
        return "Error: No character types selected."

    return ''.join(random.choice(char_set) for _ in range(length))

def generate_multiple(count, **kwargs):
    return [generate_password(**kwargs) for _ in range(count)]
