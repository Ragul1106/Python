tasks = []
tasks.append(input("Enter first task: "))
tasks.append(input("Enter second task: "))
tasks.append(input("Enter third task: "))

print("\nAll tasks:", tasks)
print("\nTasks with numbers:")
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")