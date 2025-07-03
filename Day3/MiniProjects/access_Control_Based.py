role = input("Enter your role (admin/user): ").lower()
has_id = input("Do you have ID? (yes/no): ").lower()

if role == 'admin' and has_id == 'yes':
    print("Full access granted")
elif role == 'user' and has_id == 'yes':
    print("Limited access granted")
elif not has_id == 'yes':
    print("Access denied - no ID")
else:
    print("Access denied - invalid role")