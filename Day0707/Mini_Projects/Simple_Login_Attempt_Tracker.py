correct_username = "admin"
correct_password = "password123"

for attempt in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
else:
    print("Account Locked!")