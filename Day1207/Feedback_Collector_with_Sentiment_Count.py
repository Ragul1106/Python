def analyze_feedback():
    feedbacks = []
    print("Enter feedbacks (type 'done' when finished):")
    
    while True:
        fb = input("> ")
        if fb.lower() == 'done':
            break
        feedbacks.append(fb.lower())
    
    good = sum(1 for fb in feedbacks if 'good' in fb or 'great' in fb)
    bad = sum(1 for fb in feedbacks if 'bad' in fb or 'poor' in fb)
    neutral = len(feedbacks) - good - bad
    
    print("\nFeedback Analysis:")
    print(f"Positive: {good}")
    print(f"Negative: {bad}")
    print(f"Neutral: {neutral}")

analyze_feedback()