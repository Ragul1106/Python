import time
import random
import os
from functools import wraps

SAMPLE_TEXTS = [
    "Python is a powerful programming language.",
    "Practice typing to increase your speed and accuracy.",
    "Always write clean and readable code.",
    "Typing fast is a useful and fun skill to master.",
    "Focus on accuracy before speed."
]

HIGHSCORE_FILE = "high_scores.txt"
results_history = []

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\n⏱️ Start typing after the prompt appears...")
        input("Press Enter to begin...\n")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        result['time'] = round(end - start, 2)
        result['wpm'] = round((result['correct_chars'] / 5) / (result['time'] / 60), 2)
        results_history.append(result)
        return result
    return wrapper

def word_generator(text):
    for word in text.split():
        yield word

@timed
def run_typing_test():
    text = random.choice(SAMPLE_TEXTS)
    print(f"\n📝 Type the following:\n{text}\n")
    user_input = input("Your input: ").strip()

    correct_chars = sum(1 for a, b in zip(text, user_input) if a == b)
    total_chars = len(text)

    return {
        'typed': user_input,
        'original': text,
        'correct_chars': correct_chars,
        'total_chars': total_chars
    }

def save_score(wpm):
    try:
        with open(HIGHSCORE_FILE, "a") as f:
            f.write(f"{wpm}\n")
    except Exception as e:
        print(f"❌ Error saving high score: {e}")

def load_scores():
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            return [float(line.strip()) for line in f if line.strip()]
    except Exception as e:
        print(f"❌ Error loading scores: {e}")
        return []

def main():
    while True:
        print("\n🔸 1. Start Typing Test\n🔸 2. View High Scores\n🔸 3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            result = run_typing_test()
            print(f"\n✅ Test Completed!")
            print(f"Time: {result['time']}s")
            print(f"Accuracy: {result['correct_chars']} / {result['total_chars']} characters")
            print(f"Speed: {result['wpm']} WPM")
            save_score(result['wpm'])

        elif choice == '2':
            scores = load_scores()
            if scores:
                print("\n🏆 High Scores:")
                for i, score in enumerate(sorted(scores, reverse=True)[:5], start=1):
                    print(f"{i}. {score} WPM")
            else:
                print("\n❌ No scores found.")

        elif choice == '3':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
