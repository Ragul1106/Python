resumes = {}

def add_resume(resume_id, skills, experience):
    resumes[resume_id] = {"skills": skills, "experience": experience}

def search_by_skills(skills_needed):
    return [rid for rid, data in resumes.items() 
            if all(skill in data["skills"] for skill in skills_needed)]

add_resume(1, ["Python", "SQL"], 3)
print("Python devops:", search_by_skills(["Python"]))