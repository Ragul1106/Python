email = input("Enter email: ")
valid = (email.find('@') > 5 and 
         email.endswith('gmail.com') and 
         email.count('@') == 1)
print("Valid" if valid else "Invalid")