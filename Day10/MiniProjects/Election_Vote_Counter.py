votes = {}

def cast_vote(candidate):
    votes[candidate] = votes.get(candidate, 0) + 1

def winner():
    return max(votes.items(), key=lambda x: x[1])[0]

cast_vote("Ragul")
print("Winner:", winner())