def is_valid_email(email):
    if '@' not in email or '.' not in email:
        return False
    
    username, domain = email.split('@', 1)
    if not username or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    if len(username) < 3 or len(domain) < 5:
        return False
    
    return True

while True:
    email = input("Enter email address: ")
    if is_valid_email(email):
        print("Valid email!")
        break
    print("Invalid email. Please try again.")