# Task 31: Create a CSV file containing student names and marks.
def task_31():
    import csv
    students = [["Name", "Marks"], ["Alice", 85], ["Bob", 78], ["Charlie", 92]]
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students)

# Task 32: Read the CSV file and print names of students who scored >80.
def task_32():
    import csv
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if int(row[1]) > 80:
                print(row[0])

# Task 33: Append new student data to the CSV file.
def task_33():
    import csv
    with open("students.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["David", 88])

# Task 34: Read a CSV and convert it into a dictionary of student names and marks.
def task_34():
    import csv
    student_dict = {}
    with open("students.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            student_dict[row["Name"]] = int(row["Marks"])
    print(student_dict)

# Task 35: Create a report summarizing highest and average marks using a CSV file.
def task_35():
    import csv
    marks = []
    with open("students.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks.append(int(row["Marks"]))
    print("Highest:", max(marks))
    print("Average:", sum(marks) / len(marks))