name = input("Enter your name: ").strip().upper()
age = input("Enter your age: ").strip()
job = input("Enter your job title: ").strip()

bio = f"Hi, I'm {name}. I'm {age} years old and I work as a {job}"
print(bio)
print(f"Bio length: {len(bio)} characters")