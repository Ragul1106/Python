price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount_code = input("Enter discount code (if any): ")

valid_codes = ['SALE10', 'SALE20']

subtotal = price * quantity
discount = 0

if discount_code in valid_codes:
    if discount_code == 'SALE10':
        discount = subtotal * 0.1
    elif discount_code == 'SALE20':
        discount = subtotal * 0.2

total = subtotal - discount

print(f"\nSubtotal: ₹{subtotal:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Total: ₹{total:.2f}")