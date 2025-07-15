feedback = {}

def add_feedback(cust_id, text, rating):
    feedback[cust_id] = {"feedback": text, "rating": rating}

def average_rating():
    ratings = [data["rating"] for data in feedback.values()]
    return sum(ratings) / len(ratings) if ratings else 0

def positive_feedback():
    return {cid: data for cid, data in feedback.items() 
            if data["rating"] > 4}

add_feedback(101, "Great service!", 5)
print("Avg rating:", average_rating())