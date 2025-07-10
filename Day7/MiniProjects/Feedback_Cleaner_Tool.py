feedback = input("Enter feedback: ").strip().replace('!', '')
print(f"Cleaned: {feedback}")
print(f"Word count: {len(feedback.split())}")
print(f"Character count: {len(feedback)}")