feedbacks = input("Enter feedback messages (separated by |): ").split('|')

for feedback in feedbacks:
    print(f"'{feedback.strip()}': {'Positive' if 'good' in feedback.lower() else 'Neutral'}")