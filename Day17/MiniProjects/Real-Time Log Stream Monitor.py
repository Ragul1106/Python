import time

def log_monitor(filename, keywords=["ERROR", "WARNING"]):
    with open(filename, 'r') as file:
        file.seek(0, 2)  
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  
                continue
            if any(keyword in line for keyword in keywords):
                yield line.strip()

# try:
#     for alert in log_monitor('app.log'):
#         print(f"ALERT: {alert}")
# except KeyboardInterrupt:
#     print("Monitoring stopped")