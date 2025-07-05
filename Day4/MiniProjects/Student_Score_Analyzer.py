scores = []
for i in range(5):
    scores.append(int(input(f"Enter score {i+1}: ")))
maximum = scores[0]
minimum = scores[0]
total = 0
for score in scores:
    if score > maximum:
        maximum = score
    if score < minimum:
        minimum = score
    total += score
average = total / len(scores)
print(f"Highest: {maximum}, Lowest: {minimum}, Average: {average}")