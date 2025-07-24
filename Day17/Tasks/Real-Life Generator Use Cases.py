import time
import random

# 1. Log file reader
def log_reader(filename):
    with open(filename) as file:
        for line in file:
            if line.strip(): 
                yield line.strip()

# 2. Sensor data simulator
def sensor_simulator():
    while True:
        yield random.uniform(0, 100)
        time.sleep(1)

# 3. API pagination mock
def api_paginator(total_items, per_page=10):
    for i in range(0, total_items, per_page):
        yield {"data": list(range(i, min(i+per_page, total_items))), "page": i//per_page + 1}

# 4. Stock price simulator
def price_monitor():
    price = 100.0
    while True:
        change = random.uniform(-2, 2)
        price = max(0.1, price + change)
        yield round(price, 2)
        time.sleep(0.5)

# 5. Form validation simulator
def form_validator(fields):
    for field in fields:
        is_valid = bool(random.getrandbits(1))  
        yield (field, is_valid)