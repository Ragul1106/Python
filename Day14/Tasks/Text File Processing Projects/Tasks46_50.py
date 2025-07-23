# Task 46: Build a To-Do List app that saves tasks to a .txt file and retrieves them.
def task_46():
    def add_task(task):
        with open("todo.txt", "a") as f:
            f.write(task + "\n")

    def show_tasks():
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task.strip()}")

    add_task("Buy groceries")
    add_task("Read a book")
    show_tasks()

# Task 47: Create a program that merges two text files into one.
def task_47():
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
        content = f1.read() + "\n" + f2.read()
    with open("merged.txt", "w") as f:
        f.write(content)

# Task 48: Build a script that converts .txt to .pdf using file reading and a package like fpdf.
def task_48():
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    with open("sample.txt", "r") as f:
        for line in f:
            pdf.cell(200, 10, txt=line.strip(), ln=True)
    pdf.output("output.pdf")

# Task 49: Implement a file difference checker that compares two files line by line.
def task_49():
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i, (l1, l2) in enumerate(zip(lines1, lines2), 1):
            if l1 != l2:
                print(f"Line {i} differs:\nFile1: {l1.strip()}\nFile2: {l2.strip()}")

# Task 50: Write a program that saves a diary entry daily in a file named by date (e.g., 2025-07-22.txt).
def task_50():
    from datetime import datetime
    filename = datetime.now().strftime("%Y-%m-%d.txt")
    entry = input("Write your diary entry: ")
    with open(filename, "a") as f:
        f.write(entry + "\n")
