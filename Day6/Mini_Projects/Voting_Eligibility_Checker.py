def check_eligibility(age):
    is_eligible = lambda a: a >= 18
    return "Eligible" if is_eligible(age) else "Not eligible"

print(check_eligibility(20))  
print(check_eligibility(16))  