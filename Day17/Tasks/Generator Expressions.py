# 1. Squares generator expression
squares = (x**2 for x in range(1, 11))

# 2. Odd numbers generator expression
odds = (x for x in [1,2,3,4,5] if x % 2 != 0)

# 3. Convert to list
gen = (x for x in range(5))
as_list = list(gen)

# 4. Long words filter
sentence = "Generator expressions are concise"
long_words = (word for word in sentence.split() if len(word) > 5)

# 5. Uppercase letters
text = "PyThOn"
uppers = (char for char in text if char.isupper())

# 6. Memory comparison
import sys
list_comp = [x for x in range(1000000)]
gen_exp = (x for x in range(1000000))
print(sys.getsizeof(list_comp))
print(sys.getsizeof(gen_exp))

# 7. Sum with generator
total = sum(x for x in range(1, 101))

# 8. Filter floats
mixed = [1, 2.5, 'a', 3.7, 4]
floats = (x for x in mixed if isinstance(x, float))

# 9. Any divisible by 3
numbers = [2, 4, 6, 8]
has_div3 = any(x % 3 == 0 for x in numbers)

# 10. Max with generator
max_num = max(x for x in [5, 2, 8, 1, 3])