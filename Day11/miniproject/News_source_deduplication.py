api1 = {'Headline A', 'Headline B'}
api2 = {'Headline B', 'Headline C'}

duplicates = api1 & api2
unique = api1 | api2
print(f"Found {len(duplicates)} duplicates")
print("Unique headlines:", unique)