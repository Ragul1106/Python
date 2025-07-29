authenticated = False

def login(password):
    global authenticated
    authenticated = True
    return password

def logged_in(func):
    def wrapper(*args, **kwargs):
        if not authenticated:
            print("🔒 Please login first!")
            return
        return func(*args, **kwargs)
    return wrapper
