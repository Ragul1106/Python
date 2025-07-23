# Task 1: Create a new text file and write a welcome message.
def task_1():
    with open("welcome.txt", "w") as f:
        f.write("Welcome to file handling in Python!")

# Task 2: Open a file, write multiple lines, and close it manually.
def task_2():
    f = open("lines.txt", "w")
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.close()

# Task 3: Use the with statement to read a file without manually closing it.
def task_3():
    with open("welcome.txt", "r") as f:
        print(f.read())

# Task 4: Read the contents of a file using .read().
def task_4():
    with open("lines.txt", "r") as f:
        content = f.read()
        print(content)

# Task 5: Read a file line-by-line using .readline().
def task_5():
    with open("lines.txt", "r") as f:
        print(f.readline())
        print(f.readline())

# Task 6: Read all lines of a file into a list using .readlines().
def task_6():
    with open("lines.txt", "r") as f:
        lines = f.readlines()
        print(lines)

# Task 7: Write a function that takes user input and appends it to a file.
def task_7():
    def append_input(filename):
        user_input = input("Enter text to append: ")
        with open(filename, "a") as f:
            f.write(user_input + "\n")

    append_input("user_input.txt")

# Task 8: Write and overwrite a file using 'w' mode.
def task_8():
    with open("overwrite.txt", "w") as f:
        f.write("This will overwrite the file.")

# Task 9: Append data to a file using 'a' mode and then display the full content.
def task_9():
    with open("append.txt", "a") as f:
        f.write("Appending new line.\n")
    with open("append.txt", "r") as f:
        print(f.read())

# Task 10: Use 'x' mode to create a file, and handle the error if it already exists.
def task_10():
    try:
        with open("newfile.txt", "x") as f:
            f.write("New file created.")
    except FileExistsError:
        print("File already exists.")