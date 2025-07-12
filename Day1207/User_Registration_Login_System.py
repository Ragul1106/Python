users = []

def register():
    username = input("Enter username: ")
    if any(u['username'] == username for u in users):
        print("Username already exists!")
        return
    
    password = input("Enter password: ")
    users.append({'username': username, 'password': password})
    print("Registration successful!")

def login():
    attempts = 3
    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")
        
        for user in users:
            if user['username'] == username and user['password'] == password:
                print("Login successful!")
                return True
        
        attempts -= 1
        print(f"Invalid credentials. {attempts} attempts left.")
    return False

def show_users():
    print("\nRegistered Users:")
    for user in users:
        print(user['username'])

while True:
    print("\n1. Register\n2. Login\n3. Show Users\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        register()
    elif choice == '2':
        if login():
            break
    elif choice == '3':
        show_users()
    elif choice == '4':
        break
    else:
        print("Invalid choice")