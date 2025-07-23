import csv
import os

FILENAME = "student_marks.csv"

def ensure_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Roll No", "Marks"])
        print("✅ CSV file created with headers.")

def add_student(name, roll, marks):
    ensure_file()
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, marks])
    print("✅ Student added.")

def view_students():
    ensure_file()
    with open(FILENAME, mode="r") as file:
        reader = list(csv.reader(file))
        if len(reader) <= 1:
            print("No records yet.")
            return
        print("\n📋 Student Records:")
        for row in reader[1:]:
            print(f"Name: {row[0]}, Roll: {row[1]}, Marks: {row[2]}")

def calculate_average():
    ensure_file()
    with open(FILENAME, mode="r") as file:
        reader = list(csv.reader(file))[1:]
        if not reader:
            print("No data to calculate average.")
            return
        total = sum(float(row[2]) for row in reader)
        average = total / len(reader)
        print(f"📊 Average Marks: {average:.2f}")

def find_topper():
    ensure_file()
    with open(FILENAME, mode="r") as file:
        reader = list(csv.reader(file))[1:]
        if not reader:
            print("No data to find topper.")
            return
        topper = max(reader, key=lambda x: float(x[2]))
        print(f"🏆 Topper: {topper[0]} (Roll: {topper[1]}) - Marks: {topper[2]}")

if __name__ == "__main__":
    while True:
        print("\n=== Student Marks Recorder ===")
        print("1. Add Student")
        print("2. View Records")
        print("3. Average Marks")
        print("4. Find Topper")
        print("5. Exit")
        try:
            choice = input("Choose option: ")
            if choice == "1":
                name = input("Enter name: ")
                roll = input("Enter roll number: ")
                marks = input("Enter marks: ")
                add_student(name, roll, marks)
            elif choice == "2":
                view_students()
            elif choice == "3":
                calculate_average()
            elif choice == "4":
                find_topper()
            elif choice == "5":
                break
            else:
                print("❌ Invalid option.")
        except FileNotFoundError:
            print("🚫 File not found.")
