# Task 36: Save user profile data (name, age, skills) into a .json file.
def task_36():
    import json
    profile = {
        "name": "Alice",
        "age": 25,
        "skills": ["Python", "Flask", "SQL"]
    }
    with open("profile.json", "w") as f:
        json.dump(profile, f, indent=4)

# Task 37: Read a .json file and display all user profiles.
def task_37():
    import json
    with open("profile.json", "r") as f:
        data = json.load(f)
        print(data)

# Task 38: Add a new entry into the existing .json data and save it back.
def task_38():
    import json
    with open("profile.json", "r") as f:
        data = json.load(f)
    data["email"] = "alice@example.com"
    with open("profile.json", "w") as f:
        json.dump(data, f, indent=4)

# Task 39: Build a mini phonebook app using .json as the database.
def task_39():
    import json
    phonebook = {"Ragul": "1234567890", "Meenu": "9876543210"}
    with open("phonebook.json", "w") as f:
        json.dump(phonebook, f, indent=4)
    with open("phonebook.json", "r") as f:
        print(json.load(f))

# Task 40: Validate if a .json file contains required keys and handle errors.
def task_40():
    import json
    required_keys = {"name", "age", "skills"}
    try:
        with open("profile.json", "r") as f:
            data = json.load(f)
        if not required_keys.issubset(data):
            raise KeyError("Missing required keys")
        print("All keys present.")
    except (json.JSONDecodeError, KeyError) as e:
        print("Validation Error:", e)
