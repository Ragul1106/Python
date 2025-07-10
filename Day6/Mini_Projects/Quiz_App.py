def quiz_app():
    questions = [
        ("Capital of France?", "Paris"),
        ("2+2?", "4"),
        ("Largest planet?", "Jupiter")
    ]
    score = 0
    
    def ask_question(q, a):
        nonlocal score
        if input(q + " ") == a:
            score += 1
            return True
        return False
    
    for q, a in questions:
        ask_question(q, a)
    
    return score

print(f"Your score: {quiz_app()}/{3}")