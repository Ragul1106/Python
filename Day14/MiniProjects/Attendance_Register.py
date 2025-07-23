import csv
from datetime import datetime
import os

FILENAME = "attendance.csv"

def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    file_exists = os.path.exists(FILENAME)

    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Date", "Time"])
        writer.writerow([name, date, time])
    print(f"✅ Attendance marked for {name} at {date} {time}")

def generate_report(name):
    if not os.path.exists(FILENAME):
        print("❌ Attendance file does not exist.")
        return

    print(f"\n📄 Attendance Report for {name}:")
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print(f"- {row['Date']} at {row['Time']}")

def main():
    print("📋 Employee Attendance Register")
    while True:
        print("\n1. Mark Attendance\n2. Generate Report\n3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter employee name: ").strip()
            mark_attendance(name)
        elif choice == "2":
            name = input("Enter employee name for report: ").strip()
            generate_report(name)
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
