tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!")

def show_tasks():
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["completed"] else " "
        print(f"{i}. [{status}] {t['task']}")

def complete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        tasks[index]["completed"] = True
        print("Task marked complete!")
    except (ValueError, IndexError):
        print("Invalid task number")

while True:
    print("\n1. Add Task\n2. Show Tasks\n3. Complete Task\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice")