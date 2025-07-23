# Task 11: Rewrite a script using with to ensure file auto-closing.
def task_11():
    with open("lines.txt") as f:
        for line in f:
            print(line.strip())

# Task 12: Demonstrate reading and writing a binary file using 'wb' and 'rb'.
def task_12():
    with open("binary.dat", "wb") as f:
        f.write(b"Binary content")
    with open("binary.dat", "rb") as f:
        print(f.read())

# Task 13: Build a file reader that checks if a file is readable or writable.
def task_13():
    with open("welcome.txt", "r") as f:
        print("Readable:", f.readable())
        print("Writable:", f.writable())

# Task 14: Create a function that returns the number of words, lines, and characters in a file.
def task_14():
    def file_summary(filename):
        with open(filename, "r") as f:
            content = f.read()
            words = len(content.split())
            lines = content.count("\n") + 1
            chars = len(content)
            return words, lines, chars
    print(file_summary("lines.txt"))

# Task 15: Create a report file that logs the time when a user logs in and out.
def task_15():
    from datetime import datetime
    with open("log.txt", "a") as f:
        f.write(f"Login: {datetime.now()}\n")
        f.write(f"Logout: {datetime.now()}\n")

# Task 16: Open a file and count how many times a specific word appears.
def task_16():
    word = "line"
    count = 0
    with open("lines.txt", "r") as f:
        for l in f:
            count += l.lower().count(word.lower())
    print(f"'{word}' appears {count} times")

# Task 17: Replace a word in a file with another word and save the result.
def task_17():
    with open("lines.txt", "r") as f:
        content = f.read().replace("Line", "Sentence")
    with open("replaced.txt", "w") as f:
        f.write(content)

# Task 18: Copy contents from one file to another file using file read and write.
def task_18():
    with open("lines.txt", "r") as src, open("copy.txt", "w") as dst:
        dst.write(src.read())

# Task 19: Reverse the contents of a file line by line and save into a new file.
def task_19():
    with open("lines.txt", "r") as f:
        reversed_lines = [line.strip()[::-1] for line in f]
    with open("reversed.txt", "w") as f:
        f.write("\n".join(reversed_lines))

# Task 20: Write and read structured data using writelines() and readlines().
def task_20():
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    with open("writelines.txt", "w") as f:
        f.writelines(lines)
    with open("writelines.txt", "r") as f:
        print(f.readlines())