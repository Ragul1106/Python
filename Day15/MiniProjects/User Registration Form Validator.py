import logging
import re

logging.basicConfig(filename='registration.log', level=logging.ERROR)

class PasswordTooWeakError(Exception):
    pass

def validate_registration(name, email, age, password):
    try:
        assert isinstance(name, str), "Name must be a string"
        assert isinstance(email, str), "Email must be a string"
        
        if not isinstance(age, int) or age < 13:
            raise ValueError("Age must be integer and at least 13")
            
        if len(password) < 8 or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password):
            raise PasswordTooWeakError("Password must be 8+ chars with uppercase and number")
            
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")
            
    except (ValueError, TypeError, AssertionError, PasswordTooWeakError) as e:
        logging.error(f"Registration failed: {e}")
        raise
    else:
        print("Registration successful!")
    finally:
        print("Validation complete")

try:
    validate_registration("Alice", "alice@example.com", 25, "Pass1234")
except Exception as e:
    print(f"Error: {e}")