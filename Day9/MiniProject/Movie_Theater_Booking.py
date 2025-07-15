seats = (
    ("A1", "A2", "A3", "A4"),
    ("B1", "B2", "B3", "B4"),
    ("C1", "C2", "C3", "C4")
)

booked = {"A1", "B3", "C2"}

print("Available seats:")
for row in seats:
    for seat in row:
        if seat not in booked:
            print(seat, end=" ")
    print()

try:
    seats[0][0] = "X1"
except TypeError:
    print("\nCannot modify seats - tuples are immutable")