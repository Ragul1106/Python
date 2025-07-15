quiz_data = [
    ("S1001", (85, 90, 78)),
    ("S1002", (72, 88, 65)),
    ("S1003", (95, 92, 89))
]

def analyze_scores():
    for student in quiz_data:
        sid, scores = student
        best = max(scores)
        worst = min(scores)
        print(f"\nStudent {sid}:")
        print(f"Scores: {scores}")
        print(f"Best: {best}, Worst: {worst}")

analyze_scores()

print("\nLast 2 attempts:")
for sid, scores in quiz_data:
    print(f"{sid}: {scores[-2:]}")