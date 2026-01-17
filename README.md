# AI Resume & Career Platform

An end-to-end **AI-powered Resume Builder and Career Guidance Platform** built using **Python and Streamlit**.  
This project helps students and job seekers generate professional resumes, cover letters, calculate ATS match scores, and receive career suggestions based on skills and job descriptions.

---

## 🚀 Features

- 📄 **AI Resume Generation**
- ✉️ **Automatic Cover Letter Generation**
- 📊 **ATS Match Score Calculation**
- 🧠 **Skill Gap Detection (Missing Skills)**
- 🎯 **Career Suggestions based on Skills**
- 📥 **Download Resume as PDF & DOCX**
- 🎨 **Multiple Resume Templates**
- 🌐 **Streamlit-based Interactive UI**

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **ML / NLP**: Scikit-learn (TF-IDF, Cosine Similarity)  
- **File Export**: ReportLab (PDF), python-docx (DOCX)  
- **Version Control**: Git & GitHub  

---

## 📁 Project Structure

ai-resume-career-platform/
│
├── app.py # Main Streamlit app
├── resume_engine.py # Resume, ATS, career logic
├── ats.py # ATS scoring utilities
├── ml_model.py # ML / NLP helpers
├── file_export.py # PDF & DOCX generation
├── file_utils.py # Utility helpers
├── docx_pdf.py # Document formatting
├── requirements.txt # Project dependencies
├── .gitignore # Ignored files
└── README.md # Project documentation



---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/ai-resume-career-platform.git
cd ai-resume-career-platform

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run app.py


Open in browser:

http://localhost:8501


Sample Input (Student JSON)
{
  "name": "Dhrams",
  "education": "B.Tech Computer Science (2021–2025), XYZ Institute of Technology, Bangalore | CGPA: 8.62",
  "skills": ["Python", "Machine Learning", "NLP", "AI", "Streamlit", "SQL"],
  "projects": ["AI Resume Builder", "Smart Crop Recommendation System", "Chatbot using NLP"],
  "experience": "AI Development Internship – Built ML models and NLP pipelines",
  "job_role": "AI Engineer"
}
