import random
mobile = input("Enter mobile: ")
last_four = mobile[-4:]
letters = random.choices('0987654321', k=2)
otp = last_four[:2] + letters[0] + last_four[2:] + letters[1]
print(f"Your OTP: {otp}")