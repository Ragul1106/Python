from functools import wraps

def require_login(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get('is_logged_in'):
            raise PermissionError("User not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

@require_login
def view_profile(user):
    print(f"Showing profile for {user['name']}")

user = {'name': 'Ragul', 'is_logged_in': True}
guest = {'name': 'Guest', 'is_logged_in': False}

view_profile(user)  
view_profile(guest) 