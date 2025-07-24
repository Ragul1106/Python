import re
import logging

logging.basicConfig(filename='email_validation.log', level=logging.ERROR)

class InvalidEmailFormatError(Exception):
    pass

def validate_emails(email_list):
    valid_emails = []
    
    for email in email_list:
        try:
            if not isinstance(email, str):
                raise TypeError("Email must be a string")
                
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                raise InvalidEmailFormatError(f"Invalid email format: {email}")
                
            valid_emails.append(email)
            
        except (TypeError, InvalidEmailFormatError) as e:
            logging.error(str(e))
            print(e)
    
    print(f"Valid emails: {valid_emails}")
    return valid_emails

emails = [
    "alice@example.com",
    "bob@invalid",
    12345,
    "charlie@domain.co.uk",
    "dave@.com"
]

validate_emails(emails)