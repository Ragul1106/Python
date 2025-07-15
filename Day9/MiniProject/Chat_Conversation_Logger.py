chat = [
    ("2023-05-01 10:15:23", ("Ragul", "Hi there!")),
    ("2023-05-01 10:16:45", ("Heera", "Hello Ragul!")),
    ("2023-05-01 10:17:12", ("Ragul", "How are you?"))
]

print("Recent messages:")
for timestamp, (sender, msg) in chat[-5:]:
    print(f"[{timestamp}] {sender}: {msg}")

user = "Ragul"
count = sum(1 for _, (sender, _) in chat if sender == user)
print(f"\n{user} sent {count} messages")