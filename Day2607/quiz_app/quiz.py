import json
import random
import time

def load_questions(filename="questions.json"):
    with open(filename, "r") as f:
        return json.load(f)

def filter_by_difficulty(questions, level):
    return [q for q in questions if q['difficulty'].lower() == level.lower()]

def run_quiz(questions, timed=False):
    score = 0
    total = len(questions)
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}/{total}")
        print(q['question'])

        if q["type"] == "mcq":
            for idx, opt in enumerate(q["options"], 1):
                print(f"{idx}. {opt}")
            try:
                start = time.time()
                ans = input("Enter option number: ")
                if timed and time.time() - start > 15:
                    print("⏰ Time's up!")
                    continue
                selected = q["options"][int(ans)-1]
            except:
                print("❌ Invalid input")
                continue
        elif q["type"] == "truefalse":
            try:
                start = time.time()
                selected = input("Enter True or False: ").capitalize()
                if timed and time.time() - start > 10:
                    print("⏰ Time's up!")
                    continue
            except:
                selected = ""
        else:
            print("❌ Unknown question type.")
            continue

        if selected == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. Answer: {q['answer']}")
    return score, total
