class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
    
    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary()")
    
    @staticmethod
    def calculate_tax(salary):
        return salary * 0.15  

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary - Employee.calculate_tax(self.monthly_salary)

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        gross_salary = self.hourly_rate * self.hours_worked
        return gross_salary - Employee.calculate_tax(gross_salary)

class Payroll:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def process_payroll(self):
        for employee in self.employees:
            salary = employee.calculate_salary()
            print(f"Paying {employee.name} (ID: {employee.emp_id}): ${salary:.2f}")