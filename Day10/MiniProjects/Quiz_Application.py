quiz = {
    "Capital of France?": {
        "options": ["London", "Paris", "Berlin"],
        "answer": "Paris"
    }
}

def take_quiz():
    score = 0
    for q, data in quiz.items():
        print(q)
        for i, opt in enumerate(data["options"], 1):
            print(f"{i}. {opt}")
        answer = input("Your answer: ")
        if answer == data["answer"]:
            score += 1
    print(f"Score: {score}/{len(quiz)}")

take_quiz()