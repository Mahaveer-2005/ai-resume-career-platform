import streamlit as st
import json
from resume_engine import generate_resume, generate_cover_letter, career_suggestions, ats_score, extract_missing_skills, career_roadmap
from file_export import create_docx, create_pdf
import os

st.set_page_config(page_title="AI Resume & Career Platform", layout="wide")

st.title("AI Resume & Career Platform")

job_desc = st.text_area("Paste Job Description (Optional)")

sample_json = """{
  "name": "Dhrams",
  "education": "B.Tech Computer Science (2021–2025), XYZ Institute of Technology, Bangalore | CGPA: 8.62",
  "skills": ["Python", "Machine Learning", "NLP", "AI", "Streamlit", "SQL"],
  "projects": ["AI Resume Builder", "Smart Crop Recommendation System", "Chatbot using NLP"],
  "experience": "AI Development Internship – Built ML models, NLP pipelines and deployed Streamlit apps",
  "job_role": "AI Engineer"
}"""

data_input = st.text_area("Student JSON Input", sample_json, height=250)

template = st.selectbox(
    "Choose Resume Template",
    ["Modern Professional", "ATS Optimized", "Creative Tech", "Corporate Executive", "Student Fresher"]
)

if st.button("Generate Resume"):
    try:
        data = json.loads(data_input)

        resume = generate_resume(data, job_desc, template)
        cover = generate_cover_letter(data)
        careers = career_suggestions(data["skills"])

        # Generate files
        create_docx(resume)
        create_pdf(resume)

        # ---------------- HEADER ----------------
        st.markdown(f"# **{resume['name']}**")
        st.markdown(f"### {resume['role']}")
        st.markdown("---")

        # ---------------- SUMMARY ----------------
        st.markdown("## **PROFESSIONAL SUMMARY**")
        st.write(resume["summary"])
        st.markdown("---")

        # ---------------- SKILLS ----------------
        st.markdown("## **TECHNICAL SKILLS**")
        st.write(resume["skills"])   # <-- FIXED (NO join here)
        st.markdown("---")

        # ---------------- PROJECTS ----------------
        st.markdown("## **PROJECT EXPERIENCE**")
        for p in resume["projects"]:
            st.write(f"- {p}")
        st.markdown("---")

        # ---------------- EXPERIENCE ----------------
        st.markdown("## **WORK EXPERIENCE**")
        st.write(resume["experience"])
        st.markdown("---")

        # ---------------- EDUCATION ----------------
        st.markdown("## **EDUCATION**")
        st.write(resume["education"])
        st.markdown("---")

        # ---------------- ATS ----------------
        if job_desc.strip() == "":
            job_desc = resume["role"] + " " + resume["skills"]

        score = ats_score(resume["summary"] + " " + resume["skills"], job_desc)

        st.markdown("## **ATS MATCH SCORE**")
        st.success(f"{score}% Match")

        missing = extract_missing_skills(resume["summary"] + " " + resume["skills"], job_desc)
        if missing:
            st.warning("Missing skills: " + ", ".join(missing))

        st.markdown("---")

        # ---------------- CAREERS ----------------
        st.markdown("## **CAREER SUGGESTIONS**")
        st.write(", ".join(careers))
        st.markdown("---")

        # ---------------- ROADMAP ----------------
        st.markdown("## **CAREER ROADMAP**")
        for step in career_roadmap(resume["role"]):
            st.write(f"• {step}")
        st.markdown("---")

        # ---------------- COVER LETTER ----------------
        st.markdown("## **COVER LETTER**")
        st.text(cover)
        st.markdown("---")

        # ---------------- DOWNLOADS ----------------
        if os.path.exists("resume.docx"):
            with open("resume.docx", "rb") as f:
                st.download_button("📄 Download DOCX", f, "resume.docx")

        if os.path.exists("resume.pdf"):
            with open("resume.pdf", "rb") as f:
                st.download_button("📑 Download PDF", f, "resume.pdf")

    except Exception as e:
        st.error(f"Error: {e}")
