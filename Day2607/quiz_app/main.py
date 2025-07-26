from quiz import load_questions, filter_by_difficulty, run_quiz

def main():
    print("🎯 Welcome to the Quiz App!")
    questions = load_questions()

    print("\nChoose Difficulty:")
    level = input("easy / medium / hard: ").strip().lower()
    filtered = filter_by_difficulty(questions, level)

    if not filtered:
        print("No questions for that level.")
        return

    timed_mode = input("Enable timed mode? (yes/no): ").lower() == "yes"

    score, total = run_quiz(filtered, timed=timed_mode)
    print(f"\n🎉 Quiz Over! Your Score: {score}/{total}")

if __name__ == "__main__":
    main()
