def generate_email():
    first = input("Enter first name: ").lower()
    last = input("Enter last name: ").lower()
    domain = input("Enter domain (e.g., example.com): ").lower()
    
    email = f"{first}.{last}@{domain}"
    print(f"\nGenerated Email: {email}")

generate_email()