import json
from functools import wraps
from datetime import datetime

def cli_logger(func):
    history = []
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        entry = {
            'timestamp': str(datetime.now()),
            'function': func.__name__,
            'args': args,
            'kwargs': kwargs
        }
        history.append(entry)
        with open('cli_history.json', 'w') as f:
            json.dump(history, f, indent=2)
        return func(*args, **kwargs)
    
    wrapper.history = history
    return wrapper

@cli_logger
def cli_command(*args, **kwargs):
    print("Executing command...")

cli_command("install", "--force", package="requests")