from task import Task
from file_ops import load_tasks, save_tasks
from decorators import timeit
from generator import due_today
from iterator import PendingIterator
from utils import is_valid_date

@timeit
def add_task(tasks):
    name = input("Task Name: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    if not is_valid_date(deadline):
        print("❌ Invalid date format.")
        return
    tasks.append(Task(name, deadline))
    save_tasks(tasks)
    print("✅ Task added!")

@timeit
def complete_task(tasks):
    name = input("Enter task name to mark as complete: ")
    found = False
    for task in tasks:
        if task.name == name and not task.status:
            task.status = True
            found = True
            break
    if found:
        save_tasks(tasks)
        print("✅ Task marked as complete.")
    else:
        print("❌ Task not found or already completed.")

@timeit
def delete_task(tasks):
    name = input("Enter task name to delete: ")
    tasks = [t for t in tasks if t.name != name]
    save_tasks(tasks)
    print("🗑️ Task deleted (if it existed).")
    return tasks

@timeit
def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
        return
    for task in tasks:
        print(task)

@timeit
def view_pending(tasks):
    print("\n🔄 Pending Tasks:")
    for task in PendingIterator(tasks):
        print(task)

@timeit
def view_due_today(tasks):
    print("\n📅 Tasks Due Today:")
    for task in due_today(tasks):
        print(task)

def menu():
    tasks = load_tasks()
    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. View Pending Tasks")
        print("6. View Tasks Due Today")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            complete_task(tasks)
        elif choice == '3':
            tasks = delete_task(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            view_pending(tasks)
        elif choice == '6':
            view_due_today(tasks)
        elif choice == '0':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()
