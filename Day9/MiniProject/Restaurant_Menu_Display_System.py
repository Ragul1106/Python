menu = [
    (1, "Margherita Pizza", 350),
    (2, "Pasta Alfredo", 280),
    (3, "Garlic Bread", 120),
    (4, "Tiramisu", 180)
]

print("Menu:")
for item in menu:
    print(f"{item[0]}. {item[1]} - ₹{item[2]}")

expensive = max(menu, key=lambda x: x[2])
print(f"\nMost expensive: {expensive[1]} (₹{expensive[2]})")

try:
    menu[0][2] = 400
except TypeError:
    print("\nCannot modify menu prices - tuples are immutable")