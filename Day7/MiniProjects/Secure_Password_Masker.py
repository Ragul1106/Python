password = input("Enter password: ")
masked = password[0] + '*'*(len(password)-2) + password[-1]
print(masked)