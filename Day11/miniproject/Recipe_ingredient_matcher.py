available = {'flour', 'sugar', 'eggs'}
required = {'flour', 'sugar', 'butter'}

if available >= required:
    print("You can make this recipe!")
else:
    print("Missing ingredients:", required - available)