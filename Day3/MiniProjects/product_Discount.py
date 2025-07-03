product = input("Enter product name: ")
price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * (discount / 100)
final_price = price - discount_amount

print(f"\nProduct: {product}")
print(f"Original Price: ₹{price:.2f}")
print(f"Discount: {discount}% (₹{discount_amount:.2f})")
print(f"Final Price: ₹{final_price:.2f}")