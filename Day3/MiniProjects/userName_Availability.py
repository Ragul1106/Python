existing_usernames = ['ragul', 'ranjith', 'heera', 'harsha']

new_username = input("Enter desired username: ")

if new_username in existing_usernames:
    print("Username not available")
else:
    print("Username available!")