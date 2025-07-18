from resume_analyzer.analyzer import extract_keywords, display_applicants

applicants = {}

def main():
    while True:
        print("\n1. Add Resume\n2. View All Resumes\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            aid = input("Enter Applicant ID: ")
            name = input("Enter Name: ")
            skills = input("Enter skills (comma-separated): ")

            skill_list = [s.strip().lower() for s in skills.split(",")]
            skill_set = extract_keywords(skill_list)

            applicants[(aid.strip(),)] = {
                "name": name,
                "skills": skill_set
            }
            print(f"Resume saved for {name} with skills: {skill_set}")

        elif choice == "2":
            display_applicants(applicants)

        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
    main()
