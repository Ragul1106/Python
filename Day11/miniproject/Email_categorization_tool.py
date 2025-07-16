email_content = "Please review #urgent #bugfix for #dashboard"

def extract_tags(text):
    return {tag.strip('#') for tag in text.split() if tag.startswith('#')}

tags = extract_tags(email_content)
print("Tags:", ', '.join(tags))