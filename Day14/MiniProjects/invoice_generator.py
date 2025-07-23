import os
from datetime import datetime

INVOICE_DIR = "invoices"

def create_invoice(customer_name, items):
    if not os.path.exists(INVOICE_DIR):
        os.makedirs(INVOICE_DIR)

    invoice_id = len(os.listdir(INVOICE_DIR)) + 1
    filename = f"invoice_{invoice_id}.txt"
    filepath = os.path.join(INVOICE_DIR, filename)

    total = sum([price * quantity for item, price, quantity in items])
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "w") as f:
        f.write(f"INVOICE ID: {invoice_id}\n")
        f.write(f"Date: {now}\n")
        f.write(f"Customer: {customer_name}\n\n")
        f.write("Items:\n")
        for item, price, quantity in items:
            f.write(f"- {item}: ₹{price} x {quantity} = ₹{price * quantity}\n")
        f.write(f"\nTotal: ₹{total}\n")
    
    print(f"✅ Invoice generated: {filepath}")

def main():
    print("🧾 Auto-Generated Invoice Generator")
    customer = input("Enter customer name: ").strip()

    items = []
    while True:
        item = input("Enter item name (or 'done'): ").strip()
        if item.lower() == 'done':
            break
        try:
            price = float(input(f"Enter price for {item}: "))
            quantity = int(input(f"Enter quantity for {item}: "))
            items.append((item, price, quantity))
        except ValueError:
            print("❌ Invalid price or quantity. Try again.")

    if items:
        create_invoice(customer, items)
    else:
        print("❌ No items to invoice.")

if __name__ == "__main__":
    main()
