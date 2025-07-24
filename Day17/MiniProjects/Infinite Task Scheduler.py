import time

def task_scheduler(tasks):
    while True:
        for task in tasks:
            start_time = time.time()
            yield f"Executing {task}"
            exec_time = time.time() - start_time
            yield f"Execution time: {exec_time:.2f}s"

tasks = ["Backup DB", "Clean cache", "Send reports"]
scheduler = task_scheduler(tasks)

for _ in range(10):
    print(next(scheduler))
    time.sleep(0.5)  