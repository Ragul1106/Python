age = input("Enter your age: ")
print(f"Age type before conversion: {type(age)}")

age = int(age)
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")

print(f"Age type after conversion: {type(age)}")