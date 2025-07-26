from functools import wraps

# 1. Double and square
def double_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

def square_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper

@square_result
@double_result
def add(a, b):
    return a + b

# 2. Authentication and authorization
def authenticate(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get('authenticated'):
            raise PermissionError("Not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

def authorize(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get('role') != role:
                raise PermissionError(f"Requires {role} role")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@authenticate
@authorize('admin')
def admin_action(user):
    return "Admin action performed"

# 3. Input/output logging
def log_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Input - args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def log_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result
    return wrapper

@log_output
@log_input
def process_data(data):
    return data * 2

# 4. Reverse and uppercase
def reverse_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

def uppercase_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_string
@reverse_string
def get_message():
    return "Hello World"

# 5. HTML formatters
def p_tag(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<p>{result}</p>"
    return wrapper

def div_tag(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<div>{result}</div>"
    return wrapper

@div_tag
@p_tag
def get_text():
    return "Decorated text"



#6. CLI App Decorator Chain (Logging, Timing, Formatting)

import time
from functools import wraps

def cli_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"CLI LOG: Executing {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def cli_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"CLI TIMER: {func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper

def cli_formatter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\n║ {str(result).center(9)} ║\n"
    return wrapper

@cli_formatter
@cli_timer
@cli_logger
def cli_add(a, b):
    time.sleep(0.5)  
    return a + b

print(cli_add(3, 5))

#7. Mathematical Chain (Log Result → Check Even)
def log_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

def check_even(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        is_even = result % 2 == 0
        print(f"Even check: {'Even' if is_even else 'Odd'}")
        return result
    return wrapper

@check_even
@log_result
def multiply(x, y):
    return x * y

multiply(3, 4) 

#8. Input Validator + Result Transformer
def validate_input(*validators):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg, validator in zip(args, validators):
                if not validator(arg):
                    raise ValueError(f"Validation failed for {arg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def transform_result(transformer):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return transformer(result)
        return wrapper
    return decorator

@transform_result(lambda x: f"Result: {x}")
@validate_input(lambda x: x > 0, lambda x: x < 100)
def calculate_percentage(a, b):
    return (a / b) * 100

try:
    print(calculate_percentage(25, 50))  
    print(calculate_percentage(-5, 50))  
except ValueError as e:
    print(e)
    
# 9. Processing Pipeline with Multiple Decorators
def stage1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Stage 1: Data cleaning")
        args = [str(arg).strip() for arg in args] 
        return func(*args, **kwargs)
    return wrapper

def stage2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Stage 2: Data validation")
        if not all(arg.isalpha() for arg in args):
            raise ValueError("Only alphabetic characters allowed")
        return func(*args, **kwargs)
    return wrapper

def stage3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Stage 3: Result formatting")
        return result.upper()
    return wrapper

@stage3
@stage2
@stage1
def process_data(*words):
    return " ".join(words)

print(process_data(" hello ", " world ")) 

# 10. Preserving Metadata with functools.wraps
from functools import wraps

def decorator1(func):
    @wraps(func)  
    def wrapper(*args, **kwargs):
        """Decorator1 wrapper docstring"""
        print(f"Decorator1 processing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)  
    def wrapper(*args, **kwargs):
        """Decorator2 wrapper docstring"""
        print(f"Decorator2 processing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@decorator2
@decorator1
def original_function():
    """Original function docstring"""
    print("Original function executed")

original_function()
print("Name:", original_function.__name__)  
print("Docstring:", original_function.__doc__)  
    