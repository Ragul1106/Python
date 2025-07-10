text = input("Enter text: ")
keyword = input("Enter keyword: ")

highlighted = text.replace(keyword, keyword.upper())
count = text.lower().count(keyword.lower())

print(f"Highlighted:\n{highlighted}")
print(f"Occurrences: {count}")