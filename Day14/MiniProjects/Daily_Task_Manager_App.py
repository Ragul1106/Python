import os
from datetime import datetime

def get_today_filename():
    today = datetime.now().strftime("%Y-%m-%d")
    return f"{today}.txt"

def add_task(task):
    filename = get_today_filename()
    with open(filename, "a") as file:
        file.write(task + "\n")
    print("✅ Task added.")

def view_tasks():
    filename = get_today_filename()
    if not os.path.exists(filename):
        print("No tasks for today.")
        return
    with open(filename, "r") as file:
        tasks = file.readlines()
        print("📋 Today's Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.strip()}")


def delete_task(task_number):
    filename = get_today_filename()
    if not os.path.exists(filename):
        print("No tasks found.")
        return
    with open(filename, "r") as file:
        tasks = file.readlines()
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        with open(filename, "w") as file:
            file.writelines(tasks)
        print(f"🗑️ Deleted: {removed.strip()}")
    else:
        print("❌ Invalid task number.")


if __name__ == "__main__":
    while True:
        print("\n=== Daily Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("❗ Enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
