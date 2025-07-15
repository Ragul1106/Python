employees = {}

def add_employee(emp_id, name, dept, salary):
    employees.setdefault(emp_id, {"name": name, "dept": dept, "salary": salary})

def update_employee(emp_id, dept=None, salary=None):
    if emp_id in employees:
        if dept: employees[emp_id]["dept"] = dept
        if salary: employees[emp_id]["salary"] = salary

def search_by_dept(dept):
    return [emp for emp, data in employees.items() 
            if data["dept"] == dept]

add_employee(101, "Ragul", "IT", 50000)
print("IT employees:", search_by_dept("IT"))