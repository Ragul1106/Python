from task import Task

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as f:
            return [Task.from_line(line) for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task.to_line())
