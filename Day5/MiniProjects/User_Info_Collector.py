user_data = {}
count = 0

while count < 5:
    name = input(f"Enter name {count+1}: ").strip()
    if not name:
        continue
    
    age = input(f"Enter {name}'s age: ")
    user_data[name] = age
    count += 1
    pass  

print("\nCollected user data:")
for name, age in user_data.items():
    print(f"{name}: {age} years old")