def calculate_emi(p, r, t):
    r = r / 12 / 100  
    t = t * 12  
    emi = (p * r * (1 + r)**t) / ((1 + r)**t - 1)
    return round(emi, 2)


quick_emi = lambda p, r, t: round((p * (r/1200) * (1 + (r/1200))**(t*12) / ((1 + (r/1200))**(t*12) - 1), 2))

print(f"EMI: ₹{calculate_emi(100000, 8, 5)}")
print(f"Quick EMI: ₹{quick_emi(100000, 8, 5)}")