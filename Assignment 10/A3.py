
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text1 = "Artificial Intelligence is transforming industries through automation and learning."
text2 = "Blockchain provides secure and transparent transactions across a decentralized network."

tok1 = set(text1.lower().split())
tok2 = set(text2.lower().split())
jaccard = len(tok1 & tok2) / len(tok1 | tok2)

tfidf = TfidfVectorizer()
mat = tfidf.fit_transform([text1, text2])
cos_sim = cosine_similarity(mat[0:1], mat[1:2])[0][0]

print(jaccard)
print(cos_sim)
