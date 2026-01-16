from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

train = ["python ai nlp", "java backend", "accounting", "machine learning", "sales"]
labels = [1,0,0,1,0]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(train)

model = LogisticRegression()
model.fit(X, labels)

def predict_job_fit(resume):
    X_test = vectorizer.transform([resume])
    return model.predict(X_test)[0], round(model.predict_proba(X_test)[0][1]*100,2)
