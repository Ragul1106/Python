# Task 1: Print numbers from 1 to 10 using a while loop.
number = 1
while number <= 10:
    print(number)
    number += 1

# Task 2: Print even numbers from 2 to 20 using a while loop.
even = 2
while even <= 20:
    print(even)
    even += 2

# Task 3: Print the reverse numbers from 10 to 1.
num = 10
while num >= 1:
    print(num)
    num -= 1

# Task 4: Ask the user to enter a number and print all numbers up to that number.
limit = int(input("Enter a number: "))
i = 1
while i <= limit:
    print(i)
    i += 1

# Task 5: Calculate the sum of numbers from 1 to 50 using while.
sum_total = 0
count = 1
while count <= 50:
    sum_total += count
    count += 1
print("Sum from 1 to 50:", sum_total)

# Task 6: Find the factorial of a number using a while loop.
n = int(input("Enter a number: "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print("Factorial is:", factorial)

# Task 7: Print all multiples of 3 between 1 and 30.
multiple = 3
while multiple <= 30:
    print(multiple)
    multiple += 3

# Task 8: Take user input until they type "stop".
user_input = ""
while user_input.lower() != "stop":
    user_input = input("Enter something (type 'stop' to end): ")

# Task 9: Count from 100 down to 50 in steps of 5.
num = 100
while num >= 50:
    print(num)
    num -= 5

# Task 10: Take 5 inputs from user and store them in a list using a while loop.
values = []
count = 0
while count < 5:
    value = input("Enter a value: ")
    values.append(value)
    count += 1
print("Values entered:", values)

# Task 11: Create a while True loop that prints "Welcome!" infinitely (Manually stop it).
while True:
    print("Welcome!")

# Task 12: Create a login simulation that keeps asking for a correct password until it's matched.
password = "admin123"
while True:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted")
        break

# Task 13: Simulate a menu-based app using an infinite loop (while True) with exit option.
while True:
    print("1. Say Hello\n2. Say Bye\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Bye!")
    elif choice == "3":
        print("Exiting...")
        break

# Task 14: Continuously ask for a number until the user enters a negative number.
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break

# Task 15: Simulate an ATM system using an infinite loop with options.
balance = 1000
while True:
    print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    option = input("Choose an option: ")
    if option == "1":
        print("Balance:", balance)
    elif option == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
    elif option == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient balance")
    elif option == "4":
        break

# Task 16: Print odd numbers from 1 to 20 using continue.
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

# Task 17: Ask the user to enter 5 numbers. Skip the number if it is negative using continue.
count = 0
while count < 5:
    num = int(input("Enter a number: "))
    if num < 0:
        continue
    print("You entered:", num)
    count += 1

# Task 18: Print numbers from 1 to 10, but skip 5 using continue.
n = 1
while n <= 10:
    if n == 5:
        n += 1
        continue
    print(n)
    n += 1

# Task 19: Print all numbers from 1 to 20 except those divisible by 3.
n = 1
while n <= 20:
    if n % 3 == 0:
        n += 1
        continue
    print(n)
    n += 1

# Task 20: Ask the user to enter 10 words. Skip if the word is less than 3 characters.
words = []
i = 0
while i < 10:
    word = input("Enter a word: ")
    if len(word) < 3:
        continue
    words.append(word)
    i += 1
print("Words:", words)

# Task 21: Print only vowels from the string "python programming" using while and continue.
text = "python programming"
i = 0
while i < len(text):
    if text[i].lower() not in "aeiou":
        i += 1
        continue
    print(text[i])
    i += 1

# Task 22: Count how many odd numbers exist between 1 and 100.
count = 0
num = 1
while num <= 100:
    if num % 2 != 0:
        count += 1
    num += 1
print("Total odd numbers:", count)

# Task 23: Keep asking user for numbers and print only if it's a multiple of 5.
while True:
    number = int(input("Enter a number: "))
    if number % 5 != 0:
        continue
    print("Valid multiple of 5:", number)

# Task 24: Skip printing numbers divisible by both 2 and 3 from 1 to 30.
n = 1
while n <= 30:
    if n % 2 == 0 and n % 3 == 0:
        n += 1
        continue
    print(n)
    n += 1

# Task 25: Skip even numbers and print the cube of odd numbers between 1 and 20.
n = 1
while n <= 20:
    if n % 2 == 0:
        n += 1
        continue
    print(f"Cube of {n} = {n**3}")
    n += 1


# Task 26: Print numbers from 1 to 10 and break the loop if number is 6.
n = 1
while n <= 10:
    if n == 6:
        break
    print(n)
    n += 1

# Task 27: Ask the user to enter numbers. Break the loop when user enters 0.
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break

# Task 28: Create a simple password checker. Break the loop if the correct password is entered.
while True:
    pwd = input("Enter password: ")
    if pwd == "python123":
        print("Correct password!")
        break

# Task 29: Print numbers from 1 to 100. Break the loop when a number divisible by 17 is found.
n = 1
while n <= 100:
    if n % 17 == 0:
        print("Found divisible by 17:", n)
        break
    n += 1

# Task 30: Keep asking for user input until they type "exit" (use break to stop).
while True:
    data = input("Type something (exit to stop): ")
    if data.lower() == "exit":
        break

# Task 31: Simulate a game loop: “Press q to quit”.
while True:
    key = input("Press key (q to quit): ")
    if key.lower() == "q":
        break

# Task 32: Ask the user 10 questions, stop early if any answer is empty using break.
i = 0
while i < 10:
    answer = input(f"Answer question {i+1}: ")
    if answer == "":
        print("Empty answer. Stopping.")
        break
    i += 1

# Task 33: Simulate 3 login attempts. Break the loop if login is successful.
password = "1234"
attempts = 0
while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == password:
        print("Login successful")
        break
    attempts += 1

# Task 34: Print the multiplication table of 5, but stop if the product exceeds 30.
i = 1
while True:
    result = 5 * i
    if result > 30:
        break
    print(f"5 x {i} = {result}")
    i += 1

# Task 35: Count from 1 to 10. If number is 7, break the loop and print “Loop Interrupted”.
i = 1
while i <= 10:
    if i == 7:
        print("Loop Interrupted")
        break
    print(i)
    i += 1


# Task 36: Loop through 1 to 5 and use pass when number is 3.
i = 1
while i <= 5:
    if i == 3:
        pass
    print(i)
    i += 1

# Task 37: Simulate a placeholder loop for future features.
i = 1
while i <= 3:
    pass  # Placeholder for future feature
    i += 1
print("Feature under development")

# Task 38: Create a loop where you skip logic for even numbers using pass.
i = 1
while i <= 10:
    if i % 2 == 0:
        pass
    else:
        print(i)
    i += 1

# Task 39: Use a loop that prints numbers 1 to 5 and uses pass when number is 2 or 4.
i = 1
while i <= 5:
    if i == 2 or i == 4:
        pass
    print(i)
    i += 1

# Task 40: Create a loop that runs without errors using pass as a placeholder for missing logic.
i = 0
while i < 3:
    # Future logic to be added
    pass
    i += 1
print("Loop completed")


# Task 41: Print numbers from 1 to 3. Use else to print "Loop Finished".
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop Finished")

# Task 42: Ask the user to enter 3 numbers. Use else to say “All numbers entered successfully”.
i = 0
while i < 3:
    num = input("Enter a number: ")
    if num == "":
        break
    i += 1
else:
    print("All numbers entered successfully")

# Task 43: Run a loop to print even numbers till 10. Use break to exit early. Ensure else doesn’t run.
i = 2
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 2
else:
    print("All even numbers printed")

# Task 44: Print numbers from 1 to 5. If loop finishes without break, print “Nice job!”.
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Nice job!")

# Task 45: Create a password checker with 3 attempts. If successful, print inside else.
attempts = 0
while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == "secret":
        print("Access granted")
        break
    attempts += 1
else:
    print("Access denied")

# ✅ 🔁 Logical/Practical Looping Use-Cases (46–50)

# Task 46: Ask the user to input 5 student names using while and store them in a list.
students = []
count = 0
while count < 5:
    name = input("Enter student name: ")
    students.append(name)
    count += 1
print("Student List:", students)

# Task 47: Create a menu-driven loop for a to-do list app (add, view, remove, exit).
todo = []
while True:
    print("1. Add\n2. View\n3. Remove\n4. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        task = input("Enter task: ")
        todo.append(task)
    elif choice == "2":
        print("To-Do List:", todo)
    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in todo:
            todo.remove(task)
        else:
            print("Task not found")
    elif choice == "4":
        break

# Task 48: Ask the user to enter age of 5 people. Print how many are adults (age ≥ 18).
adults = 0
count = 0
while count < 5:
    age = int(input("Enter age: "))
    if age >= 18:
        adults += 1
    count += 1
print("Number of adults:", adults)

# Task 49: Create a quiz loop: keep asking until the user gets the correct answer.
while True:
    answer = input("What is the capital of India? ")
    if answer.lower() == "delhi":
        print("Correct!")
        break

# Task 50: Build a basic number guessing game. User keeps guessing until the correct number is entered.
import random
target = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == target:
        print("You guessed it!")
        break
    else:
        print("Try again!")
