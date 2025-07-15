pixels = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (255, 0, 0), (255, 0, 0), (128, 128, 128)
]


red = (255, 0, 0)
print(f"Red pixels: {pixels.count(red)}")

top_left = [row[:2] for row in pixels[:2]]
print("\nTop-left corner:")
for pixel in top_left:
    print(pixel)

from collections import Counter
color_counts = Counter(pixels)
print("\nMost common color:", color_counts.most_common(1)[0][0])