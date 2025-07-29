import re

def is_valid_phone(phone):
    return re.fullmatch(r'\d{10}', phone) is not None

def is_valid_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None
