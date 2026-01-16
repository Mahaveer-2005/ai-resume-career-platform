def generate_resume(data):
    name = data["name"]
    education = data["education"]
    skills = ", ".join(data["skills"])
    projects = data["projects"]
    experience = data["experience"]
    role = data["job_role"]

    project_text = ""
    for p in projects:
        project_text += f"- {p}: Designed and implemented using modern technologies to solve real-world problems.\n"

    resume = f"""
{name}

PROFESSIONAL SUMMARY
Motivated {role} with a strong academic background in {education}. 
Skilled in {skills} and experienced in building practical projects.

TECHNICAL SKILLS
{skills}

PROJECTS
{project_text}

EXPERIENCE
- {experience}

EDUCATION
- {education}
"""
    return resume.strip()
