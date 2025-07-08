correct_password = "ragul123"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    attempts -= 1
    print(f"Wrong password. {attempts} attempts left.")
else:
    print("Too many attempts! Account locked.")