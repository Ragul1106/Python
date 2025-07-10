employees = []

def add_employee(**kwargs):
    employees.append(kwargs)
    print(f"Added: {kwargs['name']} ({kwargs['role']})")
    return employees

add_employee(name="Alice", role="Developer", salary=75000)
add_employee(name="Bob", role="Manager", salary=90000)
print("\nAll employees:", employees)