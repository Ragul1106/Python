quote = input("Enter your quote (press Enter twice to finish):\n")
lines = quote.strip().count('\n') + 1
print(f"\nQuote has {lines} lines:\n{quote}")