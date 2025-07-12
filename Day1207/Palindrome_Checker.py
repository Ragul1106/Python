def is_palindrome(text):
    clean = ''.join(c.lower() for c in text if c.isalnum())
    return clean == clean[::-1]

while True:
    text = input("Enter text to check (or 'quit'): ")
    if text.lower() == 'quit':
        break
    
    if is_palindrome(text):
        print("It's a palindrome!")
    else:
        print("Not a palindrome")