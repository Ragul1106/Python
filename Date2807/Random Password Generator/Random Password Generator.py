import random
import string
from functools import wraps
from typing import Generator, List

def exclude_similar(func):
    """Decorator to exclude similar looking characters"""
    @wraps(func)
    def wrapper(*args, **kwargs):

        similar_chars = {
            'l': '1L|',
            '1': 'lL|',
            '0': 'oO',
            'o': '0O',
            'O': '0o',
            'I': '1l|',
            '|': '1lI'
        }
        
        password = func(*args, **kwargs)
        while any(char in similar_chars and 
                any(s in password for s in similar_chars[char]) 
                for char in password):
            password = func(*args, **kwargs)
        return password
    return wrapper

class PasswordGenerator:
    def __init__(self):

        self.lowercase = list(string.ascii_lowercase)
        self.uppercase = list(string.ascii_uppercase)
        self.digits = list(string.digits)
        self.symbols = list("!@#$%^&*()_-+=[]{}|;:,.<>?")
        
        self.all_chars = (
            self.lowercase + 
            self.uppercase + 
            self.digits + 
            self.symbols
        )
    
    def generate_password(self, length: int = 12) -> str:
        """Generate a single random password"""
        if length < 8:
            raise ValueError("Password length must be at least 8 characters")
        
        password = []

        password.append(random.choice(self.lowercase))
        password.append(random.choice(self.uppercase))
        password.append(random.choice(self.digits))
        password.append(random.choice(self.symbols))

        for _ in range(length - 4):
            password.append(random.choice(self.all_chars))

        random.shuffle(password)
        return ''.join(password)
    
    @exclude_similar
    def generate_clean_password(self, length: int = 12) -> str:
        """Generate password excluding similar characters"""
        return self.generate_password(length)
    
    def password_generator(self, length: int = 12) -> Generator[str, None, None]:
        """Generator: Yield infinite passwords"""
        while True:
            yield self.generate_clean_password(length)

def main():
    generator = PasswordGenerator()
    
    print("Secure Password Generator")
    print("========================")
    
    while True:
        try:
            length = input("\nEnter password length (8-64, default 12) or 'quit': ")
            
            if length.lower() == 'quit':
                print("Goodbye!")
                break
            
            length = int(length) if length else 12
            if length < 8 or length > 64:
                print("Length must be between 8 and 64")
                continue

            print("\nHere are 5 secure password options:")
            pw_gen = generator.password_generator(length)
            for i in range(5):
                print(f"{i+1}. {next(pw_gen)}")
            
            print("\nPassword strength tips:")
            print("- Use at least 12 characters for better security")
            print("- Consider using a passphrase for easier memorization")
            
        except ValueError:
            print("Please enter a valid number or 'quit'")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()