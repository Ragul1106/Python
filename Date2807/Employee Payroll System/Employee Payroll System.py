import csv
from functools import wraps
from typing import Dict, Generator

class Employee:
    def __init__(self, emp_id: str, name: str, hours: float, rate: float):
        self.emp_id = emp_id
        self.name = name
        self.hours = hours
        self.rate = rate
        self.validate_inputs()
    
    def validate_inputs(self) -> None:
        """Exception handling for negative hours/rate"""
        if self.hours < 0:
            raise ValueError("Hours worked cannot be negative")
        if self.rate < 0:
            raise ValueError("Hourly rate cannot be negative")
    
    def calculate_salary(self) -> float:
        """Compute salary with overtime bonus (1.5x rate after 40 hours)"""
        regular_hours = min(self.hours, 40)
        overtime_hours = max(self.hours - 40, 0)
        return (regular_hours * self.rate) + (overtime_hours * self.rate * 1.5)
    
    def calculate_tax(self, gross_salary: float) -> float:
        """Apply tax brackets conditionally"""
        if gross_salary <= 10000:
            return gross_salary * 0.10
        elif gross_salary <= 50000:
            return 1000 + (gross_salary - 10000) * 0.20
        else:
            return 9000 + (gross_salary - 50000) * 0.30
    
    def generate_payslip(self) -> Dict[str, str]:
        """Generate employee payslip data"""
        gross_salary = self.calculate_salary()
        tax = self.calculate_tax(gross_salary)
        net_salary = gross_salary - tax
        
        return {
            "Employee ID": self.emp_id,
            "Name": self.name,
            "Hours Worked": f"{self.hours:.2f}",
            "Hourly Rate": f"${self.rate:.2f}",
            "Gross Salary": f"${gross_salary:.2f}",
            "Tax Deducted": f"${tax:.2f}",
            "Net Salary": f"${net_salary:.2f}",
            "Overtime": "Yes" if self.hours > 40 else "No"
        }

class PayrollSystem:
    def __init__(self):
        self.employees: Dict[str, Employee] = {}
    
    def add_employee(self, emp_id: str, name: str, hours: float, rate: float) -> None:
        """Add a new employee to the system"""
        try:
            employee = Employee(emp_id, name, hours, rate)
            self.employees[emp_id] = employee
        except ValueError as e:
            print(f"Error adding employee: {e}")
    
    def generate_all_payslips(self) -> None:
        """Loops: Generate payslips for all employees"""
        if not self.employees:
            print("No employees in the system")
            return
        
        for emp_id, employee in self.employees.items():
            payslip = employee.generate_payslip()
            self.display_payslip(payslip)
    
    def display_payslip(self, payslip: Dict[str, str]) -> None:
        """Display formatted payslip"""
        print("\n" + "="*40)
        print("PAYSLIP".center(40))
        print("="*40)
        for key, value in payslip.items():
            print(f"{key:15}: {value}")
        print("="*40)
    
    def find_overtime_employees(self) -> Generator[Employee, None, None]:
        """Generator: Yield employees with overtime"""
        for employee in self.employees.values():
            if employee.hours > 40:
                yield employee
    
    def export_to_csv(self, filename: str = "payroll.csv") -> None:
        """File handling: Export payroll to CSV"""
        if not self.employees:
            print("No employees to export")
            return
        
        try:
            with open(filename, mode='w', newline='') as file:
                fieldnames = [
                    "Employee ID", "Name", "Hours Worked", "Hourly Rate",
                    "Gross Salary", "Tax Deducted", "Net Salary", "Overtime"
                ]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()
                for employee in self.employees.values():
                    writer.writerow(employee.generate_payslip())
            
            print(f"Payroll data exported to {filename}")
        except IOError as e:
            print(f"Error exporting to CSV: {e}")
    
    @admin_only
    def update_salary(self, emp_id: str, new_rate: float) -> None:
        """Update employee hourly rate (admin only)"""
        if emp_id not in self.employees:
            print(f"Employee ID {emp_id} not found")
            return
        
        try:
            self.employees[emp_id].rate = new_rate
            self.employees[emp_id].validate_inputs()
            print(f"Updated hourly rate for {self.employees[emp_id].name}")
        except ValueError as e:
            print(f"Error updating salary: {e}")

def admin_only(func):
    """Decorator: Restrict access to admin-only functions"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # In a real system, this would check user permissions
        print("\nAdmin access required for this action")
        password = input("Enter admin password: ")
        
        # Simple password check for demonstration
        if password == "admin123":
            return func(self, *args, **kwargs)
        else:
            print("Access denied. Invalid admin credentials.")
    return wrapper

def main():
    payroll = PayrollSystem()
    
    # Add some sample employees
    payroll.add_employee("E001", "John Smith", 35, 25.50)
    payroll.add_employee("E002", "Jane Doe", 45, 30.00)
    payroll.add_employee("E003", "Bob Johnson", 50, 20.75)
    payroll.add_employee("E004", "Alice Williams", 38, 22.00)
    
    while True:
        print("\nPayroll System Menu")
        print("1. View All Payslips")
        print("2. View Overtime Employees")
        print("3. Export to CSV")
        print("4. Update Employee Rate (Admin)")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            payroll.generate_all_payslips()
        elif choice == "2":
            print("\nEmployees with Overtime:")
            for i, emp in enumerate(payroll.find_overtime_employees(), 1):
                print(f"{i}. {emp.name} ({emp.hours} hours)")
        elif choice == "3":
            filename = input("Enter CSV filename (default: payroll.csv): ") or "payroll.csv"
            payroll.export_to_csv(filename)
        elif choice == "4":
            emp_id = input("Enter employee ID: ")
            try:
                new_rate = float(input("Enter new hourly rate: "))
                payroll.update_salary(emp_id, new_rate)
            except ValueError:
                print("Invalid hourly rate. Please enter a number.")
        elif choice == "5":
            print("Exiting payroll system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()