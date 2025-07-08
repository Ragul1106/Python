num = 1

while num <= 20:
    if num % 2 == 0:
        num += 1
        continue
    print(f"{num} squared is {num**2}")
    num += 1