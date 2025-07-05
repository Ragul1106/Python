numbers = []
print("Enter 10 numbers:")
for i in range(10):
    numbers.append(int(input(f"Number {i+1}: ")))
odd_numbers = []
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)