memory_value = None

def store(value):
    global memory_value
    memory_value = value

def recall():
    return memory_value

def clear():
    global memory_value
    memory_value = None
