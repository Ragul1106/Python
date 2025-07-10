full_name = input("Enter full name: ").split()
username = full_name[0][:3] + full_name[-1][-2:]
print(username)