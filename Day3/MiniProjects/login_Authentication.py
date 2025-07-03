stored_username = "admin"
stored_password = "password123"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username is stored_username and input_password is stored_password:
    print("Login successful!")
elif input_username is not stored_username:
    print("Invalid username")
else:
    print("Invalid password")