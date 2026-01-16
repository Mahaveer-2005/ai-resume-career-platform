from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def ats_score(resume, job):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume, job])
    return round(cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100, 2)

def extract_missing_skills(resume, job):
    return list(set(job.lower().split()) - set(resume.lower().split()))
