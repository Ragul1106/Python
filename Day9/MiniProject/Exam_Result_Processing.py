results = [
    ("Ragul", (85, 92, 78)),
    ("Heera", (72, 68, 81)),
    ("Ranjith", (90, 88, 95))
]

def show_results():
    for student in results:
        name, scores = student
        total = sum(scores)
        avg = total / len(scores)
        print(f"\n{name}:")
        print(f"Scores: {scores}")
        print(f"Total: {total}")
        print(f"Average: {avg:.1f}")

show_results()

subject_index = 1
print(f"\nSecond subject scores:")
for name, scores in results:
    print(f"{name}: {scores[subject_index]}")