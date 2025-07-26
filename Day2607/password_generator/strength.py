import string

def calculate_strength(password):
    length_score = len(password)
    upper = any(c in string.ascii_uppercase for c in password)
    lower = any(c in string.ascii_lowercase for c in password)
    digit = any(c in string.digits for c in password)
    symbol = any(c in string.punctuation for c in password)

    score = length_score
    score += 5 if upper else 0
    score += 5 if lower else 0
    score += 5 if digit else 0
    score += 5 if symbol else 0

    if score >= 25:
        return "Strong"
    elif score >= 18:
        return "Moderate"
    else:
        return "Weak"
