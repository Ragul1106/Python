answers = []
answers.append(input("What is the capital of France? "))
answers.append(input("What is 2 + 2? "))
answers.append(input("What is your favorite color? "))

print("\nQuiz Answers:")
for i, answer in enumerate(answers, 1):
    print(f"Answer {i}: {answer} (type: {type(answer)})")