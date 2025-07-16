required = {'read', 'write', 'execute'}
user_perms = {'read', 'write'}

if user_perms >= required:
    print("All permissions granted")
else:
    print("Missing permissions:", required - user_perms)