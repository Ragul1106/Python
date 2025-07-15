courses = [
    ("CS101", "Introduction to Programming", (4, "Prof. Smith")),
    ("MA201", "Calculus", (3, "Prof. Johnson")),
    ("PH301", "Quantum Physics", (5, "Prof. Williams"))
]

print("Courses sorted by credits:")
for code, name, (credits, _) in sorted(courses, key=lambda x: x[2][0], reverse=True):
    print(f"{code}: {name} ({credits} credits)")

prof = "Prof. Smith"
count = sum(1 for _, _, (_, faculty) in courses if faculty == prof)
print(f"\n{prof} teaches {count} courses")