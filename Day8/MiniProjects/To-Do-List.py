tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def complete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        removed = tasks.pop(index)
        print(f"Completed: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number")

def show_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print(f"\nTop priority: {tasks[:3]}")

add_task()
add_task()
complete_task()
show_tasks()