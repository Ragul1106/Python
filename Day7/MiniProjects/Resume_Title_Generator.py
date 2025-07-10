first = input("First name: ").upper()
last = input("Last name: ").upper()
role = input("Role: ").upper()

title = " | ".join([first, last, role])
print(title)