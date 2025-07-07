word = input("Enter a word: ").lower()
is_palindrome = word == word[::-1]

print(f"'{word}' is {'a palindrome' if is_palindrome else 'not a palindrome'}")