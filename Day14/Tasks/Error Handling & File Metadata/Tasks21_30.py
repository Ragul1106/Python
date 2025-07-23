# ----------------------------
# Section 3: Error Handling & File Metadata (21–30)
# ----------------------------

# Task 21: Build a file handler that checks for FileNotFoundError and handles it.
def task_21():
    try:
        with open("non_existent_file.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")

# Task 22: Display the file size and last modified date using os.path.
def task_22():
    import os
    filepath = "lines.txt"
    if os.path.exists(filepath):
        print("Size:", os.path.getsize(filepath), "bytes")
        print("Last Modified:", os.path.getmtime(filepath))

# Task 23: Write a function that checks if a file exists and has write permission.
def task_23():
    import os
    filepath = "lines.txt"
    if os.path.exists(filepath):
        print("Writable:", os.access(filepath, os.W_OK))

# Task 24: Use try-except-finally to ensure a file is always closed after operations.
def task_24():
    try:
        f = open("lines.txt", "r")
        print(f.read())
    except Exception as e:
        print("Error:", e)
    finally:
        f.close()
        print("File closed.")

# Task 25: Create a script that checks and prints the file extension of all files in a folder.
def task_25():
    import os
    folder = "."
    for filename in os.listdir(folder):
        if os.path.isfile(filename):
            print(filename, "->", os.path.splitext(filename)[1])

# Task 26: Display all .txt files from a directory using os and glob.
def task_26():
    import glob
    txt_files = glob.glob("*.txt")
    print("Text files:", txt_files)

# Task 27: Rename a file and handle the case if the new name already exists.
def task_27():
    import os
    old_name = "lines.txt"
    new_name = "renamed_lines.txt"
    if not os.path.exists(new_name):
        os.rename(old_name, new_name)
        print("File renamed.")
    else:
        print("Target file already exists.")

# Task 28: Delete a file and handle PermissionError or FileNotFoundError.
def task_28():
    import os
    try:
        os.remove("delete_me.txt")
        print("File deleted.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")

# Task 29: Use os.makedirs() to create a folder structure for organizing files.
def task_29():
    import os
    os.makedirs("organized/documents", exist_ok=True)
    print("Folders created.")

# Task 30: Move a file to another folder using shutil.
def task_30():
    import shutil
    import os
    if not os.path.exists("organized"):
        os.makedirs("organized")
    shutil.move("reversed.txt", "organized/reversed.txt")
    print("File moved.")
