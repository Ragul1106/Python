def extract_keywords(feedback):
    # Simple keyword extraction: remove common stop words
    stop_words = {"the", "is", "was", "and", "of", "a", "an", "to", "for", "it", "this"}
    words = feedback.lower().split()
    return set(word.strip(".,!?") for word in words if word not in stop_words)

def collect_feedback(db, customer_id, feedback):
    if customer_id in db:
        print("Feedback already exists for this customer.")
        return
    keywords = extract_keywords(feedback)
    db[customer_id] = {
        "feedback": feedback,
        "keywords": keywords
    }
    print("Feedback recorded successfully.")

def show_feedback(db):
    if not db:
        print("No feedback recorded yet.")
        return

    for cid, details in db.items():
        print(f"\nCustomer ID: {cid[0]}")
        print(f"Feedback: {details['feedback']}")
        print(f"Keywords: {', '.join(details['keywords'])}")
