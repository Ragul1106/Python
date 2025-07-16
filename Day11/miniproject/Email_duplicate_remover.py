raw_emails = ['a@test.com', 'b@test.com', 'a@test.com', 'c@test.com']

def clean_emails(email_list):
    unique_emails = set(email_list)
    print(f"Removed {len(email_list) - len(unique_emails)} duplicates")
    return list(unique_emails)

cleaned = clean_emails(raw_emails)
print("Is 'a@test.com' present?", 'a@test.com' in cleaned)