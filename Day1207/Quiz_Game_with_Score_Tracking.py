questions = [
    {"question": "What is 2+2?", "answer": "4"},
    {"question": "Capital of France?", "answer": "Paris"},
    {"question": "Largest planet?", "answer": "Jupiter"}
]

def run_quiz():
    score = 0
    for q in questions:
        answer = input(q["question"] + " ")
        if answer.lower() == q["answer"].lower():
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! Answer: {q['answer']}")
    
    percentage = (score / len(questions)) * 100
    print(f"\nScore: {score}/{len(questions)} ({percentage:.0f}%)")

run_quiz()