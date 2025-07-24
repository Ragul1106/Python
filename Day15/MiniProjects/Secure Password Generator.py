import random
import string

class WeakPasswordCriteriaError(Exception):
    pass

def generate_password(length=12, upper=True, digits=True, special=True):
    try:
        if length < 8:
            raise WeakPasswordCriteriaError("Password must be at least 8 characters")
            
        chars = string.ascii_lowercase
        if upper:
            chars += string.ascii_uppercase
        if digits:
            chars += string.digits
        if special:
            chars += string.punctuation
            
        if len(chars) < 16:
            raise WeakPasswordCriteriaError("Not enough character variety")
            
        password = ''.join(random.choice(chars) for _ in range(length))
        
        # Verify criteria
        if upper and not any(c.isupper() for c in password):
            raise WeakPasswordCriteriaError("Failed to include uppercase")
        if digits and not any(c.isdigit() for c in password):
            raise WeakPasswordCriteriaError("Failed to include digits")
        if special and not any(c in string.punctuation for c in password):
            raise WeakPasswordCriteriaError("Failed to include special chars")
            
    except WeakPasswordCriteriaError as e:
        print(f"Error: {e}")
        return None
    else:
        return password
    finally:
        print("Password generation attempt complete")

password = generate_password()
if password:
    print(f"Your new password: {password}")