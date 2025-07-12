user_answers = []
correct_answers = ['A', 'B', 'C', 'D']

def take_quiz():
    questions = ["Q1: ", "Q2: ", "Q3: ", "Q4: "]
    for q in questions:
        user_answers.append(input(q).upper())

def grade_quiz():
    score = 0
    for i in range(len(correct_answers)):
        if user_answers[i] == correct_answers[i]:
            score += 1
    print(f"\nScore: {score}/{len(correct_answers)}")

take_quiz()
grade_quiz()