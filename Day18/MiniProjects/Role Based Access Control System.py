from functools import wraps

def access_control(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get('role') != required_role:
                print(f"Access denied to {func.__name__} for role {user.get('role')}")
                raise PermissionError("Insufficient privileges")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@access_control("admin")
def delete_user(user):
    print(f"User deleted by {user['name']}")

admin = {"name": "Ragul", "role": "admin"}
user = {"name": "Ranjith", "role": "user"}

delete_user(admin)  
delete_user(user)   