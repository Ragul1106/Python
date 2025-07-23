import csv
from datetime import datetime
import os

QUESTIONS_FILE = "questions.csv"
SCORES_FILE = "scores.csv"

def load_questions():
    questions = []
    if not os.path.exists(QUESTIONS_FILE):
        print("❌ questions.csv file not found.")
        return questions

    with open(QUESTIONS_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            questions.append(row)
    return questions

def save_score(name, score):
    file_exists = os.path.exists(SCORES_FILE)
    with open(SCORES_FILE, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Score", "DateTime"])
        writer.writerow([name, score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def run_quiz():
    name = input("Enter your name: ").strip()
    questions = load_questions()
    if not questions:
        return

    score = 0
    for idx, q in enumerate(questions, start=1):
        print(f"\nQ{idx}: {q['question']}")
        print(f"1. {q['option1']}")
        print(f"2. {q['option2']}")
        print(f"3. {q['option3']}")
        print(f"4. {q['option4']}")
        answer = input("Your answer (1-4): ").strip()

        correct = q["answer"]
        selected = q[f"option{answer}"] if answer in ['1', '2', '3', '4'] else None
        if selected == correct:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {correct}")

    print(f"\n📝 {name}, your score is {score}/{len(questions)}")
    save_score(name, score)

if __name__ == "__main__":
    run_quiz()
