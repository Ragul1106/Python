import json
import os
import time
from functools import wraps

# ========== Decorator ==========
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"\n⏱️ You completed the quiz in {duration:.2f} seconds.")
        return result
    return wrapper

# ========== OOP ==========
class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display(self):
        print(f"\n📘 {self.question}")
        for idx, opt in enumerate(self.options, 1):
            print(f"   {idx}. {opt}")

    def is_correct(self, choice):
        return self.options[choice - 1] == self.answer

# ========== Generator ==========
def question_generator(questions):
    for q in questions:
        yield Question(q["question"], q["options"], q["answer"])

# ========== File Handling ==========
def load_questions(filepath):
    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        sample_questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Rome"],
                "answer": "Paris"
            },
            {
                "question": "Which language is used for web apps?",
                "options": ["Python", "JavaScript", "C++", "Java"],
                "answer": "JavaScript"
            },
            {
                "question": "What does HTML stand for?",
                "options": [
                    "Hyper Trainer Marking Language",
                    "Hyper Text Marketing Language",
                    "Hyper Text Markup Language",
                    "Hyper Tool Multi Language"
                ],
                "answer": "Hyper Text Markup Language"
            }
        ]
        with open(filepath, "w") as f:
            json.dump(sample_questions, f, indent=4)

    with open(filepath, "r") as f:
        return json.load(f)

# ========== Quiz Logic ==========
@timer
def start_quiz():
    questions = load_questions("quiz_data/questions.json")
    gen = question_generator(questions)

    score = 0
    total = len(questions)

    for q in gen:
        q.display()
        try:
            choice = int(input("👉 Your answer (1-4): "))
            if 1 <= choice <= 4:
                if q.is_correct(choice):
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Wrong! Correct answer: {q.answer}")
            else:
                print("⚠️ Enter a number between 1 and 4.")
        except (ValueError, IndexError):
            print("⚠️ Invalid input! Please enter a valid number.")

    print(f"\n🎉 Quiz Completed! Your Score: {score}/{total}")

# ========== Menu ==========
def menu():
    print("🧠 Welcome to the Quiz Game!")
    while True:
        print("\n1. Start Quiz\n2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            start_quiz()
        elif choice == '2':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
