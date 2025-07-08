questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is 2 + 2?",
    "Who painted the Mona Lisa?",
    "What is the largest mammal?"
]

index = 0
print("Answer the questions (type 'quit' to exit):")

while index < len(questions):
    answer = input(f"\nQ{index+1}: {questions[index]}: ")
    if answer.lower() == 'quit':
        break
    print("Good answer!" if answer else "No answer provided")
    index += 1
else:
    print("\nQuiz complete! Thanks for playing.")