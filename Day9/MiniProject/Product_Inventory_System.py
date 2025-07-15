products = [
    (101, "Laptop", 45000, 10),
    (102, "Smartphone", 25000, 25),
    (103, "Tablet", 18000, 15),
    (104, "Headphones", 5000, 30)
]

total_value = sum(price * qty for _, _, price, qty in products)
print(f"Total inventory value: ₹{total_value:.2f}")

print("\nPremium products (₹20,000+):")
for prod in products:
    if prod[2] > 20000: 
        print(f"{prod[1]} - ₹{prod[2]}")

print("\nProducts sorted by price:")
for prod in sorted(products, key=lambda x: x[2]):
    print(f"{prod[1]}: ₹{prod[2]}")