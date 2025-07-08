num = 1
odd_numbers = []

while num <= 20:
    if num % 2 == 0:
        num += 1
        continue
    odd_numbers.append(num)
    num += 1

print("Odd numbers between 1-20:", odd_numbers)