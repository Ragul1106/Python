feedbacks = []
print("Enter feedback (type 'exit' to end):")

while True:
    feedback = input("Feedback: ").strip()
    if feedback.lower() == 'exit':
        break
    if len(feedback) < 3:
        print("Feedback too short")
        continue
    feedbacks.append(feedback)

print("\nCollected feedbacks:")
for fb in feedbacks:
    print(f"- {fb}")