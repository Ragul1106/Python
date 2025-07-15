players = [
    (7, "Ronaldo", ("Forward", 25)),
    (10, "Messi", ("Forward", 18)),
    (5, "Ramos", ("Defender", 5)),
    (1, "Neuer", ("Goalkeeper", 0))
]

print("Top scorers:")
for num, name, (pos, goals) in players:
    if goals > 10:
        print(f"{name} ({pos}): {goals} goals")

strikers = sum(1 for _, _, (pos, _) in players if pos == "Forward")
print(f"\nTotal strikers: {strikers}")