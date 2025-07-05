rooms = {'Standard': 2000, 'Deluxe': 3500, 'Suite': 5000}
print("Room Types:")
for room, price in rooms.items():
    print(f"{room}: ₹{price}/night")

room_type = input("Enter room type: ")
nights = int(input("Enter number of nights: "))

total = rooms[room_type] * nights
if nights > 3:
    total *= 0.9
    print("10% discount applied!")

print(f"\nTotal Cost: ₹{total:.2f}")