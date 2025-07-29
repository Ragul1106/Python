from datetime import datetime

def due_today(tasks):
    today = datetime.today().date()
    for task in tasks:
        if not task.status and datetime.strptime(task.deadline, "%Y-%m-%d").date() == today:
            yield task
