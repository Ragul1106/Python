age = int(input("Enter your age: "))

if age < 12:
    price = 50
elif 12 <= age <= 60:
    price = 120
else:
    price = 100

print(f"\nTicket price: ₹{price}")