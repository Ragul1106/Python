from functools import wraps

def log_methods(cls):
    for name, method in cls.__dict__.items():
        if callable(method):
            @wraps(method)
            def wrapper(*args, **kwargs):
                print(f"Calling {name} with {args[1:]}, {kwargs}")
                return method(*args, **kwargs)
            setattr(cls, name, wrapper)
    return cls

@log_methods
class DataProcessor:
    def process(self, data):
        return data.upper()
    
    def analyze(self, data):
        return len(data)

processor = DataProcessor()
processor.process("test")
processor.analyze("sample")