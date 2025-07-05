tasks = ["Clean desk", "Attend meeting", "Code review", "Write report", "Client call"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day, task in zip(days, tasks):
    print(f"{day}: {task}")