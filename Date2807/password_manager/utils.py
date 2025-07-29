import random
import string

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

def weak_passwords(passwords):
    for entry in passwords:
        if len(entry["password"]) < 6:
            yield entry
