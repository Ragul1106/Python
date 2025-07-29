import re
from typing import Dict, Generator, List

class PasswordChecker:
    def __init__(self):
        self.strength_thresholds: Dict[str, int] = {
            "Very Weak": 0,
            "Weak": 2,
            "Medium": 4,
            "Strong": 6,
            "Very Strong": 8
        }
        self.criteria = [
            (r'[A-Z]', "uppercase letter"),
            (r'[a-z]', "lowercase letter"),
            (r'[0-9]', "digit"),
            (r'[^A-Za-z0-9]', "special character"),
            (r'.{8,}', "at least 8 characters"),
            (r'.{12,}', "at least 12 characters")
        ]

    def evaluate_strength(self, password: str) -> Dict[str, any]:
        """Evaluate password strength and return score and feedback"""
        if not password:
            raise ValueError("Password cannot be empty")

        score = 0
        feedback = []
        meets_criteria = []

        for pattern, description in self.criteria:
            if re.search(pattern, password):
                score += 1
                meets_criteria.append(True)
            else:
                meets_criteria.append(False)

        strength = "Very Weak"
        for level, threshold in sorted(self.strength_thresholds.items(), key=lambda x: x[1], reverse=True):
            if score >= threshold:
                strength = level
                break

        return {
            "strength": strength,
            "score": score,
            "meets_criteria": meets_criteria
        }

    def get_missing_criteria(self, password: str) -> Generator[str, None, None]:
        """Generator: Yield suggestions for missing criteria"""
        evaluation = self.evaluate_strength(password)
        for i, (pattern, description) in enumerate(self.criteria):
            if not evaluation["meets_criteria"][i] and i < 4:  
                yield f"Add a {description}"

    def get_strength_feedback(self, strength: str) -> str:
        """Get feedback based on strength level"""
        feedback = {
            "Very Weak": "This password is extremely easy to guess",
            "Weak": "This password could be easily guessed",
            "Medium": "This password provides basic protection",
            "Strong": "This password provides good protection",
            "Very Strong": "This password provides excellent protection"
        }
        return feedback.get(strength, "Unknown strength level")

def main():
    checker = PasswordChecker()

    print("Password Strength Checker")
    print("========================\n")

    while True:
        try:
            password = input("Enter a password to check (or 'quit' to exit): ").strip()

            if password.lower() == 'quit':
                print("Goodbye!")
                break

            if not password:
                raise ValueError("Password cannot be empty")

            result = checker.evaluate_strength(password)
            strength = result["strength"]
            score = result["score"]

            print(f"\nPassword Strength: {strength} (Score: {score}/{len(checker.criteria)})")
            print(f"Feedback: {checker.get_strength_feedback(strength)}")

            if strength != "Very Strong":
                print("\nTo improve your password:")
                for suggestion in checker.get_missing_criteria(password):
                    print(f"- {suggestion}")
                if not any(checker.get_missing_criteria(password)):
                    print("- Make it longer (at least 12 characters recommended)")

            if strength in ["Very Strong", "Strong"]:
                if input("\nThis is a good password! Check another? (y/n): ").lower() != 'y':
                    print("Goodbye!")
                    break
            else:
                print("\nConsider using a stronger password.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()