while True:
    password = input("Create a password (minimum 6 characters): ")
    if len(password) < 6:
        print("Password too short. Try again.")
        continue
    break
else:
    print("Password accepted!")