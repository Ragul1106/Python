def circle_area(r):
    return 3.14 * r**2 if r > 0 else "Invalid radius"

def rectangle_area(l, w):
    return l * w if l > 0 and w > 0 else "Invalid dimensions"

square_area = lambda s: s**2 if s > 0 else "Invalid side"

print(f"Circle area: {circle_area(5)}")
print(f"Rectangle area: {rectangle_area(4, 6)}")
print(f"Square area: {square_area(3)}")