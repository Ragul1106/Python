banned_words = ['spam', 'scam', 'hate']

message = input("Enter your message: ").lower()

for word in banned_words:
    if word in message:
        print("Warning: Your message contains inappropriate content")
        break
else:
    print("Message sent successfully")