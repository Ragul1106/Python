total_bill = 0  # Global variable

def calculate_total(*args):
    global total_bill
    total_bill = sum(args)
    return total_bill

def apply_discount(discount_percent):
    global total_bill
    total_bill *= (1 - discount_percent/100)
    return total_bill

# Usage
calculate_total(100, 200, 50)
print(f"Total before discount: {total_bill}")
apply_discount(10)
print(f"Total after 10% discount: {total_bill:.2f}")