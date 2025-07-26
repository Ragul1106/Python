from datetime import datetime

def sort_by_priority(tasks):
    return sorted(tasks, key=lambda x: x.priority)

def sort_by_due_date(tasks):
    return sorted(tasks, key=lambda x: datetime.strptime(x.due_date, "%Y-%m-%d"))

def search_tasks(tasks, keyword):
    return [task for task in tasks if keyword.lower() in task.title.lower()]
