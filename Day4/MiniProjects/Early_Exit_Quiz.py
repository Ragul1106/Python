questions = [
    ("What is the capital of India?", "Delhi"),
    ("2 + 2 = ?", "4"),
    ("What color is the sky?", "Blue"),
    ("What is 5 * 6?", "30"),
    ("Which planet is known as the Red Planet?", "Mars")
]
for question, answer in questions:
    user_answer = input(question + " ")
    if user_answer.strip().lower() != answer.lower():
        print("Wrong Answer. Game Over.")
        break
else:
    print("Quiz Completed!")