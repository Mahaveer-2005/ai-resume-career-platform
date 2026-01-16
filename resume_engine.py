from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def generate_resume(data, job_desc="", template="Modern Professional"):
    name = data["name"]
    role = data["job_role"]
    education = data["education"]

    # FIX: convert list → clean string
    skills_list = data["skills"]
    skills = ", ".join(skills_list)

    experience = data["experience"]
    projects = data["projects"]

    summary = (
        f"{role} with a strong academic background in {education}. "
        f"Skilled in {skills} with hands-on experience in building real-world AI solutions, "
        f"data pipelines, machine learning models, and intelligent systems."
    )

    project_list = []
    for p in projects:
        project_list.append(
            f"{p}: Designed and developed AI-based systems, implemented ML/NLP models, "
            f"and deployed real-world applications."
        )

    return {
        "name": name,
        "role": role,
        "summary": summary,
        "skills": skills,          # <-- now a string
        "projects": project_list,
        "experience": experience,
        "education": education
    }


    # --------- PROFESSIONAL SUMMARY ---------
    summary = (
        f"{role} with a strong academic background in {education}. "
        f"Skilled in {skills} with hands-on experience in building real-world AI and software solutions. "
        "Experienced in developing scalable applications, data pipelines, and intelligent systems."
    )

    # --------- PROJECT FORMATTING ---------
    projects = []
    for p in projects_list:
        projects.append(
            f"{p}: Designed, developed, and deployed AI-driven solutions to solve real-world problems, "
            "including data processing, model training, and application deployment."
        )

    # --------- TEMPLATE STYLES ---------
    if template == "ATS Optimized":
        summary = (
            f"{role} | {education}. Core skills include {skills}. "
            "Experience in machine learning, NLP, data analysis, and AI application development."
        )

    elif template == "Creative Tech":
        summary = (
            f"🚀 {role} passionate about building intelligent systems. "
            f"Expert in {skills} with experience delivering innovative AI-powered applications."
        )

    elif template == "Corporate Executive":
        summary = (
            f"Strategic {role} with strong technical leadership and academic excellence in {education}. "
            f"Expertise in {skills} and delivering enterprise-grade AI solutions."
        )

    elif template == "Student Fresher":
        summary = (
            f"Aspiring {role} with solid academic foundation in {education}. "
            f"Skilled in {skills} and eager to contribute to innovative technology teams."
        )

    return {
        "name": name,
        "role": role,
        "summary": summary,
        "skills": skills,
        "projects": projects,
        "experience": experience,
        "education": education
    }


# ---------------- COVER LETTER ----------------
def generate_cover_letter(data):
    return f"""
Dear Hiring Manager,

I am writing to apply for the position of {data.get("job_role","Professional")}. 
With a strong foundation in {", ".join(data.get("skills", []))} and hands-on experience in AI and software projects, 
I am confident that I can contribute effectively to your organization.

I have worked on real-world projects including intelligent systems, machine learning models, and NLP applications, 
which have strengthened my problem-solving and development skills.

Thank you for considering my application.

Sincerely,  
{data.get("name","")}
"""


# ---------------- CAREER SUGGESTIONS ----------------
def career_suggestions(skills):
    skills = [s.lower() for s in skills]

    if "ai" in skills or "machine learning" in skills or "nlp" in skills:
        return ["AI Engineer", "Machine Learning Engineer", "Data Scientist", "NLP Engineer"]
    if "web" in skills or "javascript" in skills:
        return ["Frontend Developer", "Full Stack Developer"]
    if "python" in skills:
        return ["Software Developer", "Automation Engineer"]
    return ["Software Engineer", "Technical Analyst"]


# ---------------- ATS MATCH SCORE ----------------
def ats_score(resume_text, job_description):
    if not job_description.strip():
        return 0.0

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)


# ---------------- MISSING SKILLS ----------------
def extract_missing_skills(resume_text, job_description):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())
    missing = job_words - resume_words
    return list(missing)


# ---------------- CAREER ROADMAP ----------------
def career_roadmap(role):
    roadmap = {
        "AI Engineer": [
            "Learn Python & Data Structures",
            "Learn Machine Learning & Deep Learning",
            "Master NLP & AI frameworks",
            "Build AI projects",
            "Deploy AI applications",
            "Apply for AI Engineer roles"
        ],
        "Data Scientist": [
            "Learn Statistics & Python",
            "Learn SQL & Data Analysis",
            "Learn Machine Learning",
            "Build Data Science projects",
            "Apply for Data Scientist roles"
        ],
        "Software Engineer": [
            "Learn Programming Fundamentals",
            "Learn Backend & Frontend",
            "Build Projects",
            "Practice Coding Interviews",
            "Apply for Jobs"
        ]
    }

    return roadmap.get(role, ["Learn Skills", "Build Projects", "Apply for Jobs"])
