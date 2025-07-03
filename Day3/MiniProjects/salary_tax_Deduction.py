salary = float(input("Enter your annual salary (in Lakhs): ")) * 100000

if salary < 500000:
    tax = 0
elif 500000 <= salary < 1000000:
    tax = salary * 0.1
else:
    tax = salary * 0.2

net_salary = salary - tax
print(f"\nGross Salary: ₹{salary:,.2f}")
print(f"Tax Deducted: ₹{tax:,.2f}")
print(f"Net Salary: ₹{net_salary:,.2f}")