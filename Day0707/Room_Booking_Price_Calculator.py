room_type = input("Enter room type (Standard/Deluxe): ").lower()
nights = int(input("Enter number of nights: "))

if room_type == 'standard':
    price = 1000
elif room_type == 'deluxe':
    price = 1500
else:
    price = 0

if price and nights > 3:
    total = price * nights * 0.8
    print("20% discount applied!")
else:
    total = price * nights

print(f"\nTotal Cost: ₹{total:.2f}")