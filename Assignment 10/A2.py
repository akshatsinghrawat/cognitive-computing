
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np

texts = ["Great phone with excellent battery life", "Poor camera quality in this phone", "Affordable price and good performance"]

cv = CountVectorizer()
bow = cv.fit_transform(texts)

tfidf = TfidfVectorizer()
tfidf_mat = tfidf.fit_transform(texts)
feature_names = tfidf.get_feature_names_out()

for i in range(len(texts)):
    scores = tfidf_mat[i].toarray().flatten()
    top_idx = scores.argsort()[-3:][::-1]
    top_words = [feature_names[j] for j in top_idx]
    print(top_words)
