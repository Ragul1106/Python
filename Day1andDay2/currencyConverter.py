usd = input("Enter amount in USD: ")
print(f"Before conversion type: {type(usd)}")

inr = float(usd) * 83
print(f"\n{usd} USD = {inr} INR")
print(f"After conversion type: {type(inr)}")
