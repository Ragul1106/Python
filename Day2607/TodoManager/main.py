from task import Task
from file_handler import save_tasks, load_tasks
from utils import sort_by_priority, sort_by_due_date, search_tasks

tasks = load_tasks()

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task.is_completed else "❌"
        print(f"{idx}. [{status}] {task.title} | Priority: {task.priority} | Due: {task.due_date}")

def add_task():
    title = input("Enter task title: ")
    priority = int(input("Enter priority (1=High, 2=Medium, 3=Low): "))
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append(Task(title, priority, due_date))
    save_tasks(tasks)
    print("Task added!")

def delete_task():
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted!")
    except (IndexError, ValueError):
        print("Invalid input.")

def mark_complete():
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        tasks[index].is_completed = True
        save_tasks(tasks)
        print("Task marked as complete!")
    except (IndexError, ValueError):
        print("Invalid input.")

def search():
    keyword = input("Enter keyword to search: ")
    result = search_tasks(tasks, keyword)
    display_tasks(result)

def sort_tasks():
    choice = input("Sort by (1) Priority or (2) Due Date? ")
    if choice == "1":
        sorted_tasks = sort_by_priority(tasks)
    else:
        sorted_tasks = sort_by_due_date(tasks)
    display_tasks(sorted_tasks)

def main():
    while True:
        print("\n📋 To-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Sort Tasks")
        print("6. Search Tasks")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_complete()
        elif choice == "5":
            sort_tasks()
        elif choice == "6":
            search()
        elif choice == "7":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
