import logging

logging.basicConfig(filename='quiz.log', level=logging.ERROR)

def quiz_game():
    questions = [
        {
            'question': "What is 2+2?",
            'options': ['A) 3', 'B) 4', 'C) 5', 'D) 6'],
            'answer': 'B'
        },
        {
            'question': "Capital of France?",
            'options': ['A) London', 'B) Berlin', 'C) Paris', 'D) Madrid'],
            'answer': 'C'
        }
    ]
    
    score = 0
    
    for q in questions:
        while True:
            try:
                print(q['question'])
                for option in q['options']:
                    print(option)
                
                answer = input("Your answer (A/B/C/D): ").upper()
                if answer not in ['A', 'B', 'C', 'D']:
                    raise ValueError("Answer must be A, B, C, or D")
                    
                if answer == q['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! Correct answer was {q['answer']}")
                break
                    
            except ValueError as e:
                logging.error(f"Invalid input: {e}")
                print(e)
    
    print(f"Your final score: {score}/{len(questions)}")

quiz_game()