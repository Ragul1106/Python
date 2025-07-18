from shift_utils.shift_ops import assign_shift, view_shifts

employee_shifts = {}

def main():
    while True:
        print("\n1. Assign Shift\n2. View Shifts\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            shift = input("Enter Shift (Morning/Evening/Night): ")
            emp_key = (emp_id,)
            assign_shift(employee_shifts, emp_key, name, shift)
        elif choice == "2":
            view_shifts(employee_shifts)
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
