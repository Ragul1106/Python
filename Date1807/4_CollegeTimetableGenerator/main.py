from timetable_utils.generator import generate_timetable, display_timetable

timetable = {}

def main():
    while True:
        print("\n1. Generate Timetable\n2. Display Timetable\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            generate_timetable(timetable)
        elif choice == "2":
            display_timetable(timetable)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
