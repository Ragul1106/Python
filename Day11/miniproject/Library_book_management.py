branch_a = {'Book1', 'Book2', 'Book3'}
branch_b = {'Book2', 'Book4'}

print("All books:", branch_a | branch_b)
print("Common books:", branch_a & branch_b)
print("Only in Branch A:", branch_a - branch_b)