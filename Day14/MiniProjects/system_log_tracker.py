import os
from datetime import datetime

LOG_DIR = "logs"
LOG_LIMIT = 10

def create_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def get_log_filename():
    date_str = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(LOG_DIR, f"{date_str}.log")

def count_lines(filename):
    if not os.path.exists(filename):
        return 0
    with open(filename, "r") as f:
        return sum(1 for _ in f)

def log_event(message):
    create_log_dir()
    log_file = get_log_filename()
    
    if count_lines(log_file) >= LOG_LIMIT:
        print(f"⚠️ Log limit reached for today ({LOG_LIMIT} entries). Rotating...")
        timestamp = datetime.now().strftime("%H%M%S")
        archived_file = log_file.replace(".log", f"_{timestamp}.log")
        os.rename(log_file, archived_file)

    with open(get_log_filename(), "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")
        print("✅ Log written.")

def monitored_function():
    log_event("Function executed.")

if __name__ == "__main__":
    monitored_function()
