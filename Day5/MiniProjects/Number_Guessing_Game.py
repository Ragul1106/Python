secret_number = 42
attempts = 5
count = 0

while count < attempts:
    guess = int(input("Guess the number (1-100): "))
    if guess == secret_number:
        print("Correct! You win!")
        break
    print("Too high!" if guess > secret_number else "Too low!")
    count += 1
else:
    print(f"Game over! The number was {secret_number}")