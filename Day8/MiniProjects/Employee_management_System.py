employees = [['E001', 'John', 'Developer'], ['E002', 'Jane', 'Manager']]

def add_employee():
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    role = input("Role: ")
    employees.append([emp_id, name, role])

def sort_employees():
    employees.sort(key=lambda x: x[1])
    print("\nEmployees sorted by name:")
    for emp in employees:
        print(f"{emp[1]} ({emp[0]}) - {emp[2]}")

add_employee()
sort_employees()