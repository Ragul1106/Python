# Task 41: Build a simple logger that writes logs with timestamps to a file.
def task_41():
    from datetime import datetime
    with open("app.log", "a") as f:
        f.write(f"[{datetime.now()}] Application started.\n")

# Task 42: Monitor a directory and write a log of any new file added (mock logic).
def task_42():
    import os
    from datetime import datetime
    watched_dir = "."
    existing_files = set(os.listdir(watched_dir))
    # Simulate new file detection
    new_files = existing_files.union({"new_mock_file.txt"}) - existing_files
    with open("dir_monitor.log", "a") as log:
        for file in new_files:
            log.write(f"[{datetime.now()}] New file added: {file}\n")

# Task 43: Track user login activity with date and time written to a log file.
def task_43():
    from datetime import datetime
    username = "ragul"
    with open("user_login.log", "a") as f:
        f.write(f"[{datetime.now()}] User '{username}' logged in.\n")

# Task 44: Record program execution steps to a log file and allow log filtering.
def task_44():
    def log(message, level="INFO"):
        from datetime import datetime
        with open("execution.log", "a") as f:
            f.write(f"[{datetime.now()}] [{level}] {message}\n")
    log("Program started")
    log("Performing task...", "DEBUG")
    log("Task completed", "INFO")

# Task 45: Rotate log files daily and archive them by date.
def task_45():
    import os
    from datetime import datetime
    import shutil

    log_file = "daily.log"
    archive_folder = "logs_archive"
    today = datetime.now().strftime("%Y-%m-%d")

    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    if os.path.exists(log_file):
        shutil.move(log_file, os.path.join(archive_folder, f"log_{today}.log"))
    with open(log_file, "w") as f:
        f.write(f"[{datetime.now()}] New log file started.\n")
