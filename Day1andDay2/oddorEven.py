number = input("Enter a number: ")
print(f"Before conversion type: {type(number)}")

number = int(number)
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

print(f"After conversion type: {type(number)}")