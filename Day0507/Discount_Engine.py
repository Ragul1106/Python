price = float(input("Enter product price: "))

if price > 2000:
    discount = 0.2
elif price > 1000:
    discount = 0.1
else:
    discount = 0

final_price = price * (1 - discount)
print(f"\nOriginal Price: ₹{price:.2f}")
print(f"Discount: {discount*100:.0f}%")
print(f"Final Price: ₹{final_price:.2f}")