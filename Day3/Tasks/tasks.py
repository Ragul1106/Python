# 🔹 🧮 Arithmetic Operators Tasks (1–8)

# Task 1: Take two numbers as input and print their addition, subtraction, multiplication, and division.
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)

# Task 2: Perform floor division and modulus of two numbers and display with f-string.
print(f"Floor Division: {first_number // second_number}, Modulus: {first_number % second_number}")

# Task 3: Use exponentiation ** to calculate power of a number.
base_number = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))
print(f"Power: {base_number ** exponent}")

# Task 4: Create a calculator that takes 2 inputs and prints all arithmetic results (+, -, *, /, //, %, **).
operand_one = float(input("Enter first operand: "))
operand_two = float(input("Enter second operand: "))
print(f"Addition: {operand_one + operand_two}, Subtraction: {operand_one - operand_two}, Multiplication: {operand_one * operand_two}, Division: {operand_one / operand_two}, Floor Division: {operand_one // operand_two}, Modulus: {operand_one % operand_two}, Power: {operand_one ** operand_two}")

# Task 5: Create a shopping app that adds the prices of 3 items.
item_price_1 = float(input("Enter price of item 1: "))
item_price_2 = float(input("Enter price of item 2: "))
item_price_3 = float(input("Enter price of item 3: "))
total_price = item_price_1 + item_price_2 + item_price_3
print("Total Price:", total_price)

# Task 6: Ask user for marks in 5 subjects and calculate average using arithmetic operators.
subject_marks = [int(input(f"Enter marks for subject {i + 1}: ")) for i in range(5)]
average_marks = sum(subject_marks) / 5
print("Average Marks:", average_marks)

# Task 7: Convert Celsius to Fahrenheit using arithmetic formula.
temp_celsius = float(input("Enter temperature in Celsius: "))
temp_fahrenheit = (temp_celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {temp_fahrenheit}")

# Task 8: Use print(f"") to show result of each arithmetic operation with two variables.
value_one = 20
value_two = 3
print(f"Addition: {value_one + value_two}, Subtraction: {value_one - value_two}, Multiplication: {value_one * value_two}, Division: {value_one / value_two}")

# 🔹 🧮 Comparison Operators Tasks (9–14)

# Task 9: Compare two user-input numbers using all 6 comparison operators and print results.
comparison_number_1 = int(input("Enter first number: "))
comparison_number_2 = int(input("Enter second number: "))
print(comparison_number_1 == comparison_number_2, comparison_number_1 != comparison_number_2, comparison_number_1 > comparison_number_2, comparison_number_1 < comparison_number_2, comparison_number_1 >= comparison_number_2, comparison_number_1 <= comparison_number_2)

# Task 10: Write a program to check if a person is older than 18.
person_age = int(input("Enter age: "))
print("Adult" if person_age > 18 else "Minor")

# Task 11: Take two strings and check if they are equal or not using ==, !=.
first_string = input("Enter first string: ")
second_string = input("Enter second string: ")
print("Equal" if first_string == second_string else "Not Equal")

# Task 12: Ask for two exam scores and compare which one is higher using >, <.
exam_score_1 = int(input("Enter score for Exam 1: "))
exam_score_2 = int(input("Enter score for Exam 2: "))
print("Exam 1 has higher score" if exam_score_1 > exam_score_2 else "Exam 2 has higher score")

# Task 13: Use >= and <= to check if the number lies in a particular range.
range_input = int(input("Enter a number: "))
print("In range" if 10 <= range_input <= 20 else "Out of range")

# Task 14: Create a simple program to check if a user entered score is a passing mark (above 50).
user_score = int(input("Enter your score: "))
print("Pass" if user_score > 50 else "Fail")

# 🔹 🔐 Logical Operators Tasks (15–20)

# Task 15: Use and to check if age is above 18 and the person has an ID.
user_age = int(input("Enter age: "))
has_id_card = input("Do you have an ID card? (yes/no): ")
print("Allowed" if user_age > 18 and has_id_card == "yes" else "Denied")

# Task 16: Use or to check if a user entered "yes" or "y" as confirmation.
confirmation = input("Enter confirmation (yes/y): ")
print(confirmation == "yes" or confirmation == "y")

# Task 17: Use not to reverse a comparison result.
is_greater = 5 > 10
print(not is_greater)

# Task 18: Create a program to allow club entry only if age ≥ 21 and dress code is “formal”.
club_age = int(input("Enter your age: "))
dress_code = input("Enter your dress code: ")
print("Entry allowed" if club_age >= 21 and dress_code == "formal" else "Entry denied")

# Task 19: Ask user two boolean inputs and evaluate them using all logical operators.
bool_input_one = input("Enter True/False for first value: ") == "True"
bool_input_two = input("Enter True/False for second value: ") == "True"
print("AND:", bool_input_one and bool_input_two, "OR:", bool_input_one or bool_input_two, "NOT First Value:", not bool_input_one)

# Task 20: Combine multiple conditions using and/or and print pass/fail logic.
exam_marks = int(input("Enter exam marks: "))
attendance_percentage = int(input("Enter attendance percentage: "))
print("Pass" if exam_marks >= 40 and attendance_percentage >= 75 else "Fail")

# 🔹 🖊️ Assignment Operators Tasks (21–26)

# Task 21: Initialize a variable with 10 and use +=, -=, *=, /=, //=, %= to update its value.
assignment_value = 10
assignment_value += 5
assignment_value -= 3
assignment_value *= 2
assignment_value /= 4
assignment_value //= 2
assignment_value %= 3
print("Final Value:", assignment_value)

# Task 22: Take a number and increment it by 5 using +=.
increment_number = int(input("Enter a number to increment: "))
increment_number += 5
print("Incremented value:", increment_number)

# Task 23: Calculate area of a square and double it using *=.
square_side = int(input("Enter side of square: "))
square_area = square_side * square_side
square_area *= 2
print("Doubled area of square:", square_area)

# Task 24: Take a salary amount and apply tax deduction using -=.
gross_salary = float(input("Enter salary amount: "))
tax_amount = float(input("Enter tax deduction: "))
gross_salary -= tax_amount
print("Net salary after tax:", gross_salary)

# Task 25: Build a step-by-step program that modifies a variable using every assignment operator.
modification_value = 20
modification_value += 10
modification_value -= 4
modification_value *= 2
modification_value /= 2
modification_value //= 3
modification_value %= 5
print("Final result after modifications:", modification_value)

# Task 26: Create a mini bank balance simulator using assignment operators to update deposits/withdrawals.
bank_balance = 1000
bank_balance += 500  # Deposit
bank_balance -= 200  # Withdrawal
print("Updated bank balance:", bank_balance)

# 🔹 🪪 Identity Operators Tasks (27–30)

# Task 27: Compare two identical lists using is and print if they refer to the same memory.
list_a = [1, 2, 3]
list_b = list_a
print("Same memory location:", list_a is list_b)

# Task 28: Compare two different but equal lists using is not.
list_c = [1, 2, 3]
print("Different memory location despite equal content:", list_a is not list_c)

# Task 29: Show that a = b means both a is b is True (same memory) only for non-mutable objects.
integer_a = 50
integer_b = 50
print("Same memory location for immutable objects:", integer_a is integer_b)

# Task 30: Create three variables, two referencing the same list and one different, compare using is, is not.
ref_list_one = [5, 6]
ref_list_two = ref_list_one
ref_list_three = [5, 6]
print("ref_list_one is ref_list_two:", ref_list_one is ref_list_two)
print("ref_list_one is not ref_list_three:", ref_list_one is not ref_list_three)

# 🔹 📜 Membership Operators Tasks (31–35)

# Task 31: Check if a letter is present in a string using in.
check_string = "welcome"
print("'w' in check_string:", 'w' in check_string)

# Task 32: Ask user for a fruit name and check if it is in your predefined fruit list.
fruit_list = ["apple", "banana", "cherry", "mango"]
input_fruit = input("Enter fruit name: ")
print("Fruit available:", input_fruit in fruit_list)

# Task 33: Use not in to check if a number is not in a list.
number_list = [10, 20, 30, 40]
print("15 not in number_list:", 15 not in number_list)

# Task 34: Search for a word in a sentence using in and display if it’s found.
input_sentence = "Python is a powerful language."
print("'powerful' found in sentence:", 'powerful' in input_sentence)

# Task 35: Check if a key exists in a dictionary using in.
student_info = {"name": "Arun", "age": 21, "grade": "A"}
print("'age' in student_info:", 'age' in student_info)

# 🔹 🔧 Bitwise Operators Tasks (36–40)

# Task 36: Take two integers and perform bitwise AND (&), OR (|), XOR (^).
bitwise_num1 = 12
bitwise_num2 = 6
print("AND:", bitwise_num1 & bitwise_num2)
print("OR:", bitwise_num1 | bitwise_num2)
print("XOR:", bitwise_num1 ^ bitwise_num2)

# Task 37: Demonstrate NOT (~) on a positive number.
positive_number = 10
print("Bitwise NOT of 10:", ~positive_number)

# Task 38: Perform left shift << and right shift >> on a number and display binary.
shift_value = 5
print("Left shift (<<1):", shift_value << 1)
print("Right shift (>>1):", shift_value >> 1)

# Task 39: Show binary representation using bin() and apply bitwise operations.
binary_value_a = 7
binary_value_b = 3
print("Binary A:", bin(binary_value_a), "Binary B:", bin(binary_value_b))
print("A & B:", bin(binary_value_a & binary_value_b))

# Task 40: Create a bit mask simulation using bitwise operations for toggling bits.
bit_mask = 0b1100
toggle_bits = 0b1010
result_mask = bit_mask ^ toggle_bits
print("Toggled result:", bin(result_mask))

# 🔹 🧠 Conditional Statements – Basic (41–45)

# Task 41: Ask user for age and print if eligible to vote using if.
voting_age = int(input("Enter your age: "))
if voting_age >= 18:
    print("Eligible to vote")

# Task 42: Ask for age, print "Minor" if less than 18, else "Adult" using if-else.
if voting_age < 18:
    print("Minor")
else:
    print("Adult")

# Task 43: Ask for marks and print grades using:
# if ≥ 90: A, elif ≥ 80: B, elif ≥ 70: C, else: Fail
student_marks = int(input("Enter your marks: "))
if student_marks >= 90:
    print("Grade A")
elif student_marks >= 80:
    print("Grade B")
elif student_marks >= 70:
    print("Grade C")
else:
    print("Fail")

# Task 44: Ask for temperature and print:
# "Hot" if above 35, "Warm" if between 25–35, "Cool" otherwise
today_temperature = int(input("Enter current temperature: "))
if today_temperature > 35:
    print("Hot")
elif 25 <= today_temperature <= 35:
    print("Warm")
else:
    print("Cool")

# Task 45: Ask for a number and print if it is even or odd using if-else.
number_check = int(input("Enter a number: "))
if number_check % 2 == 0:
    print("Even")
else:
    print("Odd")

# 🔹 🧠 Conditional Statements – Intermediate (46–50)

# Task 46: Ask for username and password using if-else to simulate login check.
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")
if entered_username == "admin" and entered_password == "1234":
    print("Login successful")
else:
    print("Login failed")

# Task 47: Ask if it's raining (yes/no), and whether the user has an umbrella. Use nested if.
is_raining = input("Is it raining? (yes/no): ")
if is_raining == "yes":
    has_umbrella = input("Do you have an umbrella? (yes/no): ")
    if has_umbrella == "yes":
        print("You can go outside")
    else:
        print("Stay indoors")
else:
    print("Go ahead")

# Task 48: Ask user for age and nationality. Allow voting if age ≥ 18 and nationality is "Indian".
user_voting_age = int(input("Enter your age: "))
user_nationality = input("Enter your nationality: ")
if user_voting_age >= 18 and user_nationality.lower() == "indian":
    print("Eligible to vote")
else:
    print("Not eligible")

# Task 49: Build a calculator: If user chooses "add", perform addition; If "sub", perform subtraction.
operation_choice = input("Choose operation (add/sub): ")
first_input = int(input("Enter first number: "))
second_input = int(input("Enter second number: "))
if operation_choice == "add":
    print("Result:", first_input + second_input)
elif operation_choice == "sub":
    print("Result:", first_input - second_input)
else:
    print("Invalid operation")

# Task 50: Ask for exam result (marks, attendance). If marks ≥ 40 and attendance ≥ 75%, print "Passed", else "Failed".
final_marks = int(input("Enter final marks: "))
final_attendance = int(input("Enter attendance percentage: "))
if final_marks >= 40 and final_attendance >= 75:
    print("Passed")
else:
    print("Failed")
