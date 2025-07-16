taken = {'admin', 'user', 'test'}
suggestions = {'admin', 'guest', 'newuser'}

valid = suggestions - taken
print("Available usernames:", valid)