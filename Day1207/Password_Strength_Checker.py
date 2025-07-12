import string

def check_password_strength(pwd):
    if len(pwd) < 8:
        return "Too short (min 8 chars)"
    
    requirements = {
        "lowercase": any(c in string.ascii_lowercase for c in pwd),
        "uppercase": any(c in string.ascii_uppercase for c in pwd),
        "digit": any(c in string.digits for c in pwd),
        "symbol": any(c in string.punctuation for c in pwd)
    }
    
    missing = [k for k, v in requirements.items() if not v]
    if missing:
        return f"Missing: {', '.join(missing)}"
    return "Strong password!"

while True:
    password = input("Enter password (or 'quit' to exit): ")
    if password.lower() == 'quit':
        break
    
    result = check_password_strength(password)
    if result == "Strong password!":
        print(result)
        break
    print(result)