def grade_quiz(correct_answers, user_answers):
    score = 0
    for correct, user in zip(correct_answers, user_answers):
        if correct == user:
            score += 1
    
    total_questions = len(correct_answers)
    percentage = (score / total_questions) * 100
    
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    else:
        grade = 'D'
    
    return score, total_questions, percentage, grade

def main():
    correct_answers = ['A', 'C', 'B', 'D', 'A']
    user_answers = []
    
    print("Enter your answers for the quiz (A, B, C, D):")
    for i in range(len(correct_answers)):
        answer = input(f"Question {i + 1}: ").strip().upper()
        user_answers.append(answer)
    
    score, total_questions, percentage, grade = grade_quiz(correct_answers, user_answers)
    
    print(f"\nYour Score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()