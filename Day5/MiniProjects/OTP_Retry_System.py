correct_otp = "1905"
attempts = 3

while attempts > 0:
    otp = input(f"Enter OTP ({attempts} attempts left): ")
    if otp == correct_otp:
        print("OTP verified successfully!")
        break
    print("Invalid OTP")
    attempts -= 1
else:
    print("OTP failed. No attempts left.")