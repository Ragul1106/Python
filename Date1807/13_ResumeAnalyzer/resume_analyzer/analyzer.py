def extract_keywords(skill_list):
    return set(skill_list)

def display_applicants(db):
    if not db:
        print("No applicants found.")
        return
    for aid, info in db.items():
        print(f"\nApplicant ID: {aid[0]}")
        print(f"Name: {info['name']}")
        print(f"Skills: {', '.join(info['skills'])}")
