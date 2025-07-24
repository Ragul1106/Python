import re

def email_validator(emails, max_valid=10):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    valid_count = 0
    for email in emails:
        if re.match(pattern, email):
            yield email
            valid_count += 1
            if valid_count >= max_valid:
                raise StopIteration(f"Found {max_valid} valid emails")

emails = ["test@example.com", "invalid", "user@domain.org", ...]
validator = email_validator(emails)

for valid_email in validator:
    print(f"Valid: {valid_email}")