from grade_utils.calculator import add_marks, calculate_average, display_all

grades = {}

def main():
    while True:
        print("\n1. Add Marks\n2. Calculate Average\n3. Display All\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            subjects = input("Enter Subjects (comma-separated): ").split(",")
            marks = [int(input(f"Enter mark for {sub.strip()}: ")) for sub in subjects]
            sid = (student_id.strip(),)
            add_marks(grades, sid, dict(zip([s.strip() for s in subjects], marks)))

        elif choice == "2":
            student_id = input("Enter Student ID: ")
            sid = (student_id.strip(),)
            calculate_average(grades, sid)

        elif choice == "3":
            display_all(grades)

        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
